from flask import Flask, render_template, request, redirect
import base64
import requests
import json
import os

app = Flask(__name__)


#route to handle the landing page of the BitzBots website
@app.route('/')
def welcome_page():
	
	return render_template("home_page.html")


@app.route('/makestation')
def make_galbot():
	return render_template("main_page_radiotest.html")

@app.route('/makestation/formsubmit')
def submit_form():
	a = request.args.get('face')
	b = request.args.get('body')
	jpg_filename = a + b + ".jpg"
	stl_filename = a + b + ".stl"


	#if filename == "12.stl":
	#return render_template("made_bot.html", filename=filename)
	return render_template("made_bot.html", jpg_filename=jpg_filename, stl_filename=stl_filename)
	#else:
	#	return filename

@app.route('/makestation/formsubmit/uploadtoimat')
def upload_to_imat():
	print request.args.get('filename')
	thefilename = str(request.args.get('filename'))
#need to make this open the stl file specified above
	files = open(thefilename, 'rb')

	payload = {
		"useAjax": False,
		"forceEmbedding": False,
		"plugin": "PUT YOUR TOOL ID HERE, ANNE"
		#"plugin": str(TOOL_ID),
	}

	response = requests.post("http://imatsandbox.materialise.net/upload", 
		data=payload, 
		files={'file': files},
		allow_redirects=False)

	
	#print response.headers
	#return response.headers['location']
	return redirect(response.headers['location'])

if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)
