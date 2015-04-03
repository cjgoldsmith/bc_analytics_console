'use strict';

/**
 * @ngdoc function
 * @name webappApp.controller:BCCredentialCtrl
 * @description
 * # AboutCtrl
 * Controller of the webappApp
 */
angular.module('webappApp')
  .controller('BCCredentialCtrl', ['$scope', '$http', function ($scope, $http) {

    $scope.getCredentials = function() {
        $http({
          method: 'GET',
          url: '/data/bccredentials/',
          cache: false
        }).success( function(data) {
          $scope.credentials = data;
        });
    };
    $scope.getCredentials();

    $scope.addCredentials = function() {
      $http({
        method: 'POST',
        url: '/data/bccredentials/',
        cache: false,
        data: $scope.credential
      }).success( function() {
        $scope.credential = {};
        $scope.getCredentials();
      });
    };

    $scope.getAccounts = function() {
      $http({
        method: 'GET',
        url: '/data/bcaccounts/',
        cache: false
      }).success( function(data) {
        $scope.accounts = data;
      });
    };
    $scope.getAccounts();

    $scope.addAccounts = function() {
      $http({
        method: 'POST',
        url: '/data/bcaccounts/',
        cache: false,
        data: $scope.account
      }).success( function() {
        $scope.account = {};
        $scope.getAccounts();
      });
    };
  }]);