var djeneratorApp = angular.module('djeneratorApp', []);

djeneratorApp.config(['$interpolateProvider', function($interpolateProvider) {
  $interpolateProvider.startSymbol('{[');
  $interpolateProvider.endSymbol(']}');
}]);

djeneratorApp.controller('GeneratorCtrl', function ($scope, $http) {
  $http({
    method: 'GET',
    url: '/random_name'
  }).then(function successCallback(response) {
    $scope.update_name(response.data['name']);
  }, function errorCallback(response) {
    console.log('something bad happened');
  });



  $scope.update_name = function(newName) {
    $scope.random_name = newName;
  }
});
