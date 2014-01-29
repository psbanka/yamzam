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

    /*
    $scope.pageSize = 4;
    $scope.startIndex = 0;
    $scope.currentCategory = "";
    $scope.categories = [];
    $scope.wordData = {};

    $scope.isSelected = function (category) {
        return $scope.currentCategory === category;
    };

    $scope.setCategory = function (category_name) {
        $scope.currentCategory = category_name;
        $scope.words = $scope.wordData[category_name];
    };

    $scope.forward = function () {
        $scope.startIndex += 1;
    };

    // FIXME: What does this function do? It appears to have no effect.
    $scope.hideBackButton = function () {
        $scope.startIndex < 1;
    };

    $scope.backward = function () {
        $scope.startIndex -= 1;
    };

    $scope.unique = function(arr) {
        // Simple utility function to return a unique set of values
        var u = {}, a = [];
        for(var i = 0, l = arr.length; i < l; ++i){
            if(!u.hasOwnProperty(arr[i])) {
                a.push(arr[i]);
                u[arr[i]] = 1;
            }
        }
        return a;
    }

    $scope.getInterestingWords = function(url) {
        $http.get(url).success(function (data) {
            // This receives data in the following form:
            // "next": "http://localhost:8000/api/interestingwords/?page=2",
            // "results": [
            //     {
            //         "category": "http://localhost:8000/api/categories/1/",
            //         "word": "http://localhost:8000/api/words/1/",
            //         "info": "now is the time for all good men to come to the aid of their country",
            //     }, ...

            var nextUrl = data["next"];
            //var count = data["count"];
            var categories = $scope.categories;
            for (var index in data["results"]) {
                var wordData = data["results"][index];
                var category = wordData.category;
                var word = wordData.word;
                var info = wordData.info;
                categories.push(category);
                if ($scope.wordData[category] === undefined) {
                    $scope.wordData[category] = [];
                }
                $scope.wordData[category].push({
                    "word": word,
                    "info": info
                })
                if ($scope.currentCategory === "") {
                    $scope.currentCategory = category;
                }
            }
            $scope.categories = $scope.unique(categories);
            $scope.words = $scope.wordData[$scope.currentCategory];
            if (nextUrl) {
                $scope.getInterestingWords(nextUrl)
            }
        });
    },

    $scope.getInterestingWords("/api/interestingwords/?format=json");
    */
