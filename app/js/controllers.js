'use strict';

var yamzamControllers = angular.module('yamzamControllers', []);

yamzamControllers.controller('yamzamCtrl', [
    '$scope',
    '$rootScope',
    '$location',
    '$routeParams',
    'User',
    'UserProfile',
    'Emails',
    '$http',
    function($scope, $rootScope, $location, $routeParams, User, UserProfile, Emails, $http) {
        $rootScope.userId = 1;
        $rootScope.currentUser = User.query($rootScope.userId);
        $rootScope.userProfile = UserProfile.query($rootScope.userId);
        $rootScope.emails = Emails.query();;
        $rootScope.importMessage = '';


        $rootScope.articles = [
            {'title': "January 6th", "length": 223, "import": false, "imported": false},
            {'title': "Buy our DVD", "length": 96, "import": false, "imported": false},
            {'title': "Open House", "length": 123, "import": false, "imported": true},
            {'title': "Our next speaker", "length": 523, "import": false, "imported": false},
            {'title': "Eat a hot dog", "length": 323, "import": false, "imported": true},
        ];

        $rootScope.importEmail = function() {
            $http({method: 'GET', url: '/import_email'}).
                success(function(data, status, headers, config) {
                    $rootScope.importMessage = data.response;
                }).
                error(function(data, status, headers, config) {
                    if (data.response) {
                        $rootScope.importMessage = data.response;
                    } else {
                        $rootScope.importMessage = "Error importing email";
                    }
                });
        };

        $rootScope.submitUserProfile = function() {
            $rootScope.currentUser.$save();
            $rootScope.userProfile.$save();
        };

        $rootScope.selectedEmail = $rootScope.emails[$routeParams.emailId];

        $rootScope.selectEmail = function(email) {
            $location.path("import/" + email.index);
        };

    }
]);
