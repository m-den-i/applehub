angular.module('Apple', []).controller('AppleController', ['$scope', '$http', function ($scope, $http) {
    $http.get('get-apples').success(function (data) {
        // console.log(data);
        $scope.apples = data.apples;
    });
    $scope.cart = {};
    $scope.cartLength = 0;
    $scope.add = function (item, ind) {
        if (!$scope.cart[ind]){
            $scope.cart[ind] = item;
            $scope.cartLength++;
        }
    };
    $scope.remove = function (item, ind) {
        if ($scope.cart[ind]){
            delete $scope.cart[ind];
            $scope.cartLength--;
        }
    }
    $scope.buy = function () {
        alert('Bought');
    }
}]);