from flask import Flask, render_template, request

app = Flask(__name__)


#route to handle the landing page of the BotGals website
@app.route('/')
def welcome_page():
	#Eventually, put in html/css of rocket ship symbol to click to enter main page /makestation
	
	return render_template("home_page.html")

	#return "Welcome to the World of BotGals. ~~~Making robot gals since 2015~~~"


@app.route('/makestation')
def make_galbot():
	return render_template("main_page_radiotest.html")

@app.route('/makestation/formsubmit')
def submit_form():
	a = request.args.get('face')
	b = request.args.get('body')
	filename = a + b + ".stl"
	return filename
	


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)
