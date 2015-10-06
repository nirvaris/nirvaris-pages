'use strict';

/* App Module */

var dtgApp = angular.module('dtgApp', [
	'ngSanitize',
	'dtgControllers'
  /*'dtgServices'*/
]);

var dtgControllers = angular.module('dtgControllers', []);

dtgControllers.controller('SearchFormTemplateCtrl', ['$scope', '$http', '$sce', function ($scope, $http, $sce) {
	$scope.query = {};
	$scope.results = [];
		
	$http.get('/dictionary/search').success(function(data) {
		$scope.html = data;
		$scope.search_form = $sce.trustAsHtml($scope.html);
	});	

}]);


dtgControllers.controller('SearchRequestCtrl', ['$scope', '$http', function ($scope, $http, $sce) {
	$scope.keyword = '';
	$scope.results = [];

	$scope.search = function() {
		/*$http.get('/dictionary/search', { params: $scope.keyword },
	        function(response) { $scope.results = response; },
	        function(failure) { console.log("failed :(", failure); }
		);*/
		
		
		$http.post('/dictionary/search', $.param({ 
			search_input: $scope.keyword,
			csrfmiddlewaretoken: angular.element(document.getElementsByName('csrfmiddlewaretoken')[0]).val() 
		}), {headers: {'Content-Type': 'application/x-www-form-urlencoded'}}).
		then(function(response) {
			// this callback will be called asynchronously
			// when the response is available
			$scope.words = response.data; 
		}, function(response) {
			// called asynchronously if an error occurs
			// or server returns response with an error status.
			console.log("failed :(", response); 
		});
	};

}]);


dtgApp.directive('dynamic', function ($compile) {
	return {
		restrict: 'A',
		replace: true,
		link: function (scope, ele, attrs) {
			scope.$watch(attrs.dynamic, function(html) {
				ele.html(html);
				$compile(ele.contents())(scope);
			});
		}
	};
});