'use strict';

/**
 * @ngdoc overview
 * @name webappApp
 * @description
 * # webappApp
 *
 * Main module of the application.
 */
angular
  .module('webappApp', [
    'ngAnimate',
    'ngCookies',
    'ngResource',
    'ngRoute',
    'ngSanitize',
    'ngTouch'
  ])
  .config(function ($routeProvider) {
    $routeProvider
      .when('/', {
        templateUrl: 'views/main.html',
        controller: 'MainCtrl'
      })
      .when('/about', {
        templateUrl: 'views/about.html',
        controller: 'AboutCtrl'
      })
      .when('/bccred', {
        templateUrl: 'views/bc/list.html',
        controller: 'BCCredentialCtrl'
      })
      .when('/report', {
        templateUrl: 'views/report/all.html',
        controller: 'BCReportAllCtrl'
      })
      .otherwise({
        redirectTo: '/'
      });
  });
