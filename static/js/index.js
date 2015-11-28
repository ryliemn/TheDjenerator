var djeneratorApp = angular.module('djeneratorApp', []);

djeneratorApp.config(['$interpolateProvider', function($interpolateProvider) {
  $interpolateProvider.startSymbol('{[');
  $interpolateProvider.endSymbol(']}');
}]);

djeneratorApp.controller('GeneratorCtrl', function ($scope, $http, $timeout) {
  $scope.get_new_name = function() {
    $scope.fadeOut = true;
    $http({
      method: 'GET',
      url: '/random_name'
    }).then(function successCallback(response) {
      $scope.random_name = response.data['name'];
      $scope.fadeOut = false;
    }, function errorCallback(response) {
      console.log('something bad happened');
    });
  };

  $scope.get_possible_combinations = function() {
    $http({
      method: 'GET',
      url: '/possible_combinations'
    }).then(function successCallback(response) {
      $scope.possible_combinations = response.data['possible_combinations'];
    }, function errorCallback(response) {
      console.log('could not get total combinations');
    });
  };

  $scope.get_new_name();
  $scope.get_possible_combinations();
});
