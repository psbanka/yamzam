'use strict';

/* App Module */

// TODO: How do I indicate which routes require authentication?

var yamzamApp = angular.module('yamzam', [
    'yamzamControllers', 'yamzam.services', 'ngRoute', 'ngCookies',
    'yamzam.directive', 'yamzam.filters', "$strap.directives"
]);
yamzamApp.config(['$interpolateProvider',
    function($interpolateProvider) {
        $interpolateProvider.startSymbol('{[{');
        $interpolateProvider.endSymbol('}]}');
    }
]);

yamzamApp.config(['$routeProvider',
    function($routeProvider) {
        $routeProvider.
            when('/', {templateUrl: '/partials/front.html', controller: 'yamzamCtrl'}).
            when('/profile', {templateUrl: '/partials/profile.html', controller: 'yamzamCtrl'}).
            when('/manage', {templateUrl: '/partials/manage.html', controller: 'yamzamCtrl'}).
            otherwise({redirectTo: '/'});
    }
]);

yamzamApp.run( function run( $http, $cookies ){
    // For CSRF token compatibility with Django
    $http.defaults.headers.post['X-CSRFToken'] = $cookies['csrftoken'];
    $http.defaults.headers.put['X-CSRFToken'] = $cookies['csrftoken'];
})
