rouApp.controller('RouteListCtl',function($scope){});
rouApp.controller('RouteDetailCtl',function($scope,$routeParams){
    $scope.id = $routeParams.id;
})