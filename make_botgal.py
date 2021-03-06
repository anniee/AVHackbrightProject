from flask import Flask, render_template, request, redirect
import base64
import requests
import json
import os
import model

app = Flask(__name__)


#route to handle the landing page of the BitzBots website
@app.route('/')
def welcome_page():
	
	return render_template("home_page.html")

@app.route('/about')
def about():
	return render_template("about.html")

@app.route('/makestation')
def make_galbot():
	return render_template("main_page.html")
	#return render_template("main_page_radiotest.html")

@app.route('/makestation/formsubmit')
def submit_form():
	a = request.args.get('face')
	b = request.args.get('body')
	c = request.args.get('legs')
	filename1 = a + b + c + ".png"
	stl_filename = a + b + c + ".stl"


	#if filename == "12.stl":
	#return render_template("made_bot.html", filename=filename)
	return render_template("made_bot.html", png_filename=filename1)
	#else:
	#	return filename
@app.route('/gallery')
def list_bots():
	""" Gallery showing all bots"""
	bots = model.get_bots()
	return render_template("gallery.html", bot_list=bots)



@app.route('/makestaton/formsubmit/bot')
def upload_to_gallery():
	
	bot_name = request.args.get('botname')
	maker_name = request.args.get('makername')
	maker_age = request.args.get('makerage')
	imgurl = request.args.get('pngfile')
	# print imgurl
	model.make_new_bot(bot_name, maker_name, maker_age, imgurl)


	png_name = "/static/" + imgurl
	print png_name
	stl_name = imgurl.rstrip('.png') + ".stl"
	#stl_name = png.rstrip('.png') + ".stl"
	print stl_name
	return render_template("bot.html", png_filename=png_name, stl_filename=stl_name)

@app.route('/botdetails/<bot_name>')
def show_bot_deets(bot_name):
	"""This page shows the details of a specific bot, as well as giving option to purchase bot on imat"""
	botdeets = model.get_bots_by_name(bot_name)
	print botdeets
	return render_template("botdeets.html", display_bot = botdeets)

@app.route('/makestation/formsubmit/bot/uploadtoimat')
def upload_to_imat():
	print request.args.get('filename')
	thefilename = str(request.args.get('filename'))
#need to make this open the stl file specified above
	files = open(thefilename, 'rb')

	payload = {
		"useAjax": False,
		"forceEmbedding": False,
		"plugin": os.environ.get("TOOL_ID")
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
