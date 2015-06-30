from flask import Flask, make_response, send_file
from flask_restful import Resource, Api

app = Flask(__name__)

# ---------------------------------------------
# render an html page

@app.route('/')
def index():
	# return send_file('templates/index.html')
	return make_response(open('templates/index.html').read())



# ---------------------------------------------
# build out an api to call

api = Api(app)

class MyModel(Resource):
	def get(self):
		return [{'this is': 'thunder dan'}]
		# return my_model_result()

api.add_resource(MyModel, '/data')


# ---------------------------------------------

if __name__ == '__main__':
	app.run(debug=True)