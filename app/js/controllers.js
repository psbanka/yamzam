'use strict';

var yamzamControllers = angular.module('yamzamControllers', []);

yamzamControllers.controller('yamzamCtrl', [
    '$scope',
    '$rootScope',
    '$location',
    '$routeParams',
    'User',
    'UserProfile',
    function($scope, $rootScope, $location, $routeParams, User, UserProfile) {
        $rootScope.userId = 1;
        $rootScope.currentUser = User.query($rootScope.userId);
        $rootScope.userProfile = UserProfile.query($rootScope.userId);

        $rootScope.emails = [
            {'index': 1, 'subject': 'foo', 'date': '12/22/12', 'imported': true},
            {'index': 2, 'subject': 'bar', 'date': '12/22/13', 'imported': true},
            {'index': 3, 'subject': 'baz', 'date': '12/30/12', 'imported': true},
            {'index': 4, 'subject': 'waldo', 'date': '1/22/13', 'imported': false},
            {'index': 5, 'subject': 'flax', 'date': '2/2/12', 'imported': false},
            {'index': 6, 'subject': 'falx', 'date': '12/02/02', 'imported': false},
        ];

        $rootScope.articles = [
            {'title': "January 6th", "length": 223, "import": false, "imported": false},
            {'title': "Buy our DVD", "length": 96, "import": false, "imported": false},
            {'title': "Open House", "length": 123, "import": false, "imported": true},
            {'title': "Our next speaker", "length": 523, "import": false, "imported": false},
            {'title': "Eat a hot dog", "length": 323, "import": false, "imported": true},
        ];

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
