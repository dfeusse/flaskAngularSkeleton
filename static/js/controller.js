console.log('controller.js called');

app.controller('MainController', function($scope, ModelOutput) {
	// static data
	$scope.data = [
		{'whatup': 'alexa'}
	]

	// get the data out of the resource
	ModelOutput.query(function(data) {
		$scope.api = data;
	})
})