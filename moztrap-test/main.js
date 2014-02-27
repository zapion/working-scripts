angular.module('moztrap', ['restangular']);

angular.module('moztrap').controller('MainCtrl', function($scope, Restangular) {
    Restangular.setBaseUrl('https://moztrap.mozilla.org/api/v1/');
    Restangular();
});

$.getJSON("test/test.json", function(data){
    $scope.data = data;
});

console.log($scope.data);
