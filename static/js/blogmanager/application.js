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

var app = angular.module('blogmanager.blogpost', ['ngRoute']);

app.config(['$routeProvider',
    function($routeProvider) {
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
    }
]);

app.factory('dataService', function() {
  var _currentArticle = {};
  // public data
  return {
    currentArticle: _currentArticle
  };
})

app.controller('EditBlogController', [
  '$scope', '$http' , '$location' ,'$log', 'dataService' , function($scope, $http, $location, $log , dataService) {
	$log.debug(dataService.currentArticle);
	$scope.currentArticleEdit = dataService.currentArticle;

	$scope.submitEdit = function (article) {
        $log.debug( article );
        

        $http.post('/blogpost/articles/'+article.id+'/?' + article ).success( function( result , status, headers, config){
    		$log.debug(result);
    	});
    }

 }]);

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