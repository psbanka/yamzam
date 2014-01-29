'use strict';

/* Services */

angular.module('yamzam.services', []);

var yamzamServices = angular.module('yamzam.services', ['ngResource']);

yamzamServices.factory('User', ['$resource',
    function($resource){
        return $resource('users/:userid', {}, {
            query: {method:'GET', params:{userid:'1'}, isObject:true},
            save: {method:'PUT', params:{userid:'1'}, isObject:true}
        });
    }
]);

yamzamServices.factory('UserProfile', ['$resource',
    function($resource){
        return $resource('userprofiles/:userid', {}, {
            query: {method:'GET', params:{userid:'1'}, isObject:true},
            save: {method:'PUT', params:{userid:'1'}, isObject:true}
        });
    }
]);
