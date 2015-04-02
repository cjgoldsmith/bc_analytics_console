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

    $scope.get_credentials = function() {
        $http({
          method: 'GET',
          url: '/data/bccredentials/',
          cache: false
        }).success( function(data) {
          $scope.credentials = data;
        });
    };
    $scope.get_credentials();

    $scope.add_credentials = function() {
      $http({
        method: 'POST',
        url: '/data/bccredentials/',
        cache: false,
        data: $scope.credential
      }).success( function(data) {
        $scope.credential = {};
        $scope.get_credentials();
      });
    };

    $scope.get_accounts = function() {
      $http({
        method: 'GET',
        url: '/data/bcaccounts/',
        cache: false
      }).success( function(data) {
        $scope.accounts = data;
      });
    };
    $scope.get_accounts();

    $scope.add_accounts = function() {
      $http({
        method: 'POST',
        url: '/data/bcaccounts/',
        cache: false,
        data: $scope.account
      }).success( function(data) {
        $scope.account = {};
        $scope.get_accounts();
      })
    };

  }])