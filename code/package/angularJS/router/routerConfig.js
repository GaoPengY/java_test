var rouApp = angular.module("rouApp",["ngRoute"]);
rouApp.config(["$routeProvider",function($routeProvider){
    $routeProvider
        .when('/list',{
            templateUrl: 'list.html',
            controller: 'RouteListCtl'
        })
        .when('/list/:id',{
            templateUrl: 'detail.html',
            controller: 'RouteDetailCtl'
        })
        .otherwise({
            redirectTo: '/list'
        });
}]); 