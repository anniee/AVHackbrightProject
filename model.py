import sqlite3
import make_botgal

# CONN = sqlite3.connect("bots.db")
# CURSOR = CONN.cursor()
# DB = None
# CONN = None

class Bot(object):
	" " " A wrapper object that corresponds to rows in the Bots table. " " "
	def __init__(self, bot_name, maker_name, maker_age, imgurl):
		self.bot_name = bot_name
		self.maker_name = maker_name
		self.maker_age = maker_age
		self.imgurl = imgurl

	def __repr__(self):
		return "<BitzBot: %s, %s, %s>" % (self.bot_name, self.maker_name, self.maker_age)

def connect():
	conn = sqlite3.connect("bots.db")
	cursor = conn.cursor()
	return cursor
	# global DB, CONN
	# CONN = sqlite3.connect("bots.db")
	# DB = CONN.cursor()

def make_new_bot(bot_name, maker_name, maker_age, imgurl):
	
	conn = sqlite3.connect("bots.db")
	cursor = conn.cursor()

	#query = " " " INSERT INTO Bots VALUES (?, ?, ?, ?) " " "

	#curs.execute(query, (bot_name, maker_name, maker_age, imgurl))

	cursor.execute("INSERT INTO Bots VALUES (?, ?, ?, ?)", (bot_name, maker_name, maker_age, imgurl))
	#print curs.fetchone()

	conn.commit()
	conn.close()



	# return "Successfully added BitzBot: %s" %(bot_name)

def get_bots():
	""" Query the db for bitzbots, wrap each row in a bots object"""
	cursor = connect()
	query = """SELECT bot_name, maker_name, maker_age, imgurl FROM Bots"""
	cursor.execute(query)
	bot_rows = cursor.fetchall()
	
	bots = []
	for row in bot_rows:
		bot = Bot(row[0], row[1], row[2], row[3])
		bots.append(bot)
	return bots

def get_bots_by_name(bot_name):
	"""Query for a specific bot in the database by the botname"""
	cursor = connect()
	query = """SELECT bot_name, maker_name, maker_age, imgurl FROM Bots WHERE bot_name = ?;"""

	cursor.execute(query, (bot_name,))
	row = cursor.fetchone()

	botdeets = Bot(row[0], row[1], row[2], row[3])
	return botdeets
