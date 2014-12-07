var app = angular.module("app", ['ui.dashboard', 'ui.sortable']);

app.config([
    "$httpProvider", function($httpProvider) {
        return $httpProvider.defaults.headers.common["X-CSRFToken"] = CSRF_TOKEN;
    }
]);

app.service('storageService', ['$http', '$q', '$parse', function($http, $q, $parse) {
    var urlBase = '/angular_dashboard/api/dashboards/';

    this.getItem = function (key) {
        var deferred = $q.defer();
        $http.get(urlBase + key + '/')
            .success(function(data) {
                deferred.resolve(data);
            }).
            error(function(data) {
                deferred.reject(data);
            })
        return deferred.promise;
    };
    this.setItem = function(key, value) {
        value = JSON.stringify(value)
        return $http.post(urlBase + key + '/', {value: value});
    };
    this.removeItem = function(key) {
        $http.delete(urlBase + key + '/');
    };
}]);

app.controller('dashboardCtrl', ['$scope', 'storageService', function($scope, storageService) {
    widgetDefinitions = [
       {
        name: 'random',
        directive: 'wt-scope-watch',
        attrs: {
          value: 'randomValue'
        }
      }
    ];
    defaultWidgets = [
        { name: 'random' }
    ];
    storage = storageService; 

    $scope.dashboardOptions = {
        widgetButtons: true,
        widgetDefinitions: widgetDefinitions,
        defaultWidgets: defaultWidgets,
        stringifyStorage: false,
        storage: storage,
        storageId: 'woo'
    };
}]);
