'use strict';

/**
 * @ngdoc function
 * @name webappApp.controller:BCCredentialCtrl
 * @description
 * # AboutCtrl
 * Controller of the webappApp
 */
angular.module('webappApp')
  .controller('BCReportAllCtrl', ['$scope', '$http', function ($scope, $http) {

    $scope.get_all = function() {
      $http({
        method: 'GET',
        url: '/data/reports/totals/',
        cache: false
      }).success( function(data) {
        $scope.data = data;
      });
    };
    $scope.get_all();
  }]);