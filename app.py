# -*- coding: utf-8 -*-
import os
from flask import Flask
from flask import request
from twilio.rest import Client
import json, time
import requests
from websocket import create_connection
import os
import pickle

from twilio.rest import Client

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = '<TWILIO SID>'
auth_token = '<TWILIO AUTH TOKEN>'
client = Client(account_sid, auth_token)


app = Flask(__name__)
app.debug = True
queue = []

@app.route('/', methods=['POST', 'GET'])

def request_handler():

	if request.method == 'POST':
		data = (request.json)

		if len(data['activity'])==1:
			timestamp = data['timestamp']
			from_address = data['activity'][0]['fromAddress']
			to_address = data['activity'][0]['toAddress']
			blockNum =  data['activity'][0]['blockNum']
			hash =  data['activity'][0]['hash']


		else:
			for i in range(len(data['activity'])):
				timestamp = data['timestamp']
				from_address = data['activity'][i]['fromAddress']
				to_address = data['activity'][i]['toAddress']
				blockNum =  data['activity'][i]['blockNum']
				hash =  data['activity'][i]['hash']


		print("DATA: ", data)
		print("HASH: ", hash)


		message = client.messages.create(body=" \n\n TX MINED! \n\n From: " + from_address + " \n\n To: " + to_address + " \n\n @#:" + blockNum + " \n Check tx: https://rinkeby.etherscan.io/tx/" +hash ,from_='+14415267244', to='+14154230071')
		print(message.sid)


	return ("Ok")
	#return webhook(session), 200

def run():
	app.run(host='0.0.0.0', port=5000)

if __name__ == "__main__":
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port)
