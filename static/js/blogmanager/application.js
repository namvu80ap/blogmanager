var app = angular.module('blogmanager.blogpost', []);

app.controller('BlogPostController', [
  '$scope', '$http' ,'$log', function($scope, $http, $log) {
    $scope.posts = [];
    return $http.get('/blogpost/articles').then(function(result) {
      return angular.forEach(result.data, function(item) {
        $log.debug(item);
        return $scope.posts.push(item);
      });
    });
  }
]);