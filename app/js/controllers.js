'use strict';

var yamzamControllers = angular.module('yamzamControllers', []);

yamzamControllers.controller('yamzamCtrl', [
    '$scope',
    '$rootScope',
    '$http',
    'User',
    'UserProfile',
    function($scope, $rootScope, $http, User, UserProfile) {
        $rootScope.userId = 1;
        $rootScope.currentUser = User.query($rootScope.userId);
        $rootScope.userProfile = UserProfile.query($rootScope.userId);

        $rootScope.submitUserProfile = function() {
            $rootScope.currentUser.$save();
            $rootScope.userProfile.$save();
        };
    }
]);
