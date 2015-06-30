console.log('service.js called');

// not yet being used

app.factory("ModelOutput", function($resource) {
	//return $resource("http://api.myjson.com/bins/ycwq")
	return $resource("/data")
})