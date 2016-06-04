// var app = angular.module('blogmanager.blogpost', []);

// app.controller('BlogPostController', [
//   '$scope', '$http' ,'$log', function($scope, $http, $log) {
//     $scope.posts = [];
//     return $http.get('/blogpost/articles').then(function(result) {
//       return angular.forEach(result.data, function(item) {
//         $log.debug(item);
//         return $scope.posts.push(item);
//       });
//     });
//   }
// ]);

var app = angular.module('blogmanager.blogpost', ['ngRoute','ngResource'] );

// Switch UI
app.config(['$routeProvider', '$httpProvider',
    function($routeProvider, $httpProvider) {
        $routeProvider.
        when('/edit', {
            templateUrl: 'edit_article.html',
            controller: 'EditBlogController'
        }).
        when('/', {
            templateUrl: 'list_article.html',
            controller: 'BlogPostController'
        }).
        otherwise({
            redirectTo: '/'
        });

        $httpProvider.defaults.xsrfCookieName = 'csrftoken';
        $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    }
]);

//API REST Services
app.factory('ArticleServices', ['$resource', function($resource) {
return $resource('/blogpost/articles/:id/', {},
    {
        'show': { method:'GET' },
        'update': { method:'PUT' , param: {id: '@id'} },
        'delete': { method:'DELETE', param: {id: '@id'} }
    });
}]);
app.factory('ArticleFactory', ['$resource', function($resource) {
return $resource('/blogpost/articles/', {},
    {
        'query': { method:'GET'},
        'create': { method:'POST'},
    });
}]);


app.factory('dataService', function() {
  var _currentArticle = {};
  // public data
  return {
    currentArticle: _currentArticle
  };
})

app.controller('EditBlogController', [
  '$scope', 'ArticleServices' , 'ArticleFactory', '$location', '$http' ,'$log', 'dataService',
    function($scope, ArticleServices, ArticleFactory, $location, $http , $log , dataService) {
	$log.debug(dataService.currentArticle);
	$scope.currentArticleEdit = dataService.currentArticle;

	$scope.submitEdit = function (article) {
      var getArticle = ArticleServices.show({ id: article.id })
      getArticle.title = article.title;
      getArticle.content = article.content;
      // getArticle.category = 1;
      $log.debug(getArticle);
      // getArticle.$save();
      ArticleServices.update( { id: article.id+'/' }, article);
      // $log.debug(list);
    }

 }]);


// app.controller('EditBlogController', [
//   '$scope', 'ArticleServices', '$location', '$http' ,'$log', 'dataService',
//     function($scope, ArticleServices, $location, $http , $log , dataService) {
//   $log.debug(dataService.currentArticle);
//   $scope.currentArticleEdit = dataService.currentArticle;

//   $scope.submitEdit = function (article) {
//       var getArticle = ArticleServices.show({ id: article.id })

//       $log.debug(getArticle);
//     }

//  }]);

app.controller('BlogPostController', [
  '$scope', '$http' , '$location' ,'$log', 'dataService', function($scope, $http, $location, $log , dataService) {

  	$scope.currentArticle2 = dataService.currentArticle;

  	$scope.isActive = function (viewLocation) {
        return ( viewLocation === $location.path() );
    };

    $scope.goEditArticle = function (article) {
        dataService.currentArticle = article ;
        $log.debug(dataService.currentArticle);
        $location.path('/edit');
    }

  	//GET LIST
  	$scope.posts = [];
    // return $http.get('/blogpost/articles').then(function(result) {
    //   return angular.forEach(result.data, function(item) {
    //     $log.debug(item);
    //     return $scope.posts.push(item);
    //   });
    // });

    $http.get('/blogpost/articles/').success( function( result , status, headers, config){
    	angular.forEach(result, function(item) {
	        // $log.debug(item);
	        $scope.posts.push(item);
      	});
    });

}]);