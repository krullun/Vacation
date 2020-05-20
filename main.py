#necessary imports only
import logging
from kiteconnect import KiteConnect
from key import key, secret
import requests

login_url = "https://kite.trade/connect/login?v=3&api_key="+key;
#printing for ready reference

# #getting access token
# kite = KiteConnect(api_key=key)

# try:
# 	## Trying the old access token
# 	f = open('at.txt', 'r') 
# 	access_token = f.read();
# 	f.close();

# 	#initiating kite
# 	kite.set_access_token(access_token)
# except:	
# 	##Requesting user to get the new request token
# 	print('Please open this url in browser and copy the request_token from the redirected url.')
# 	print(login_url)
# 	request_token = str(input("Paste the request token here:"))
# 	data = kite.generate_session(request_token, api_secret=secret)
# 	access_token = data['access_token']
# 	#initiating kite
# 	kite.set_access_token(access_token)

# 	f = open('at.txt', 'w') 
# 	f.write(access_token);
# 	f.close();

# print(access_token)
# print(kite.holdings())


class Kite():
	def __init__(self, key, secret):
		self.kite = KiteConnect(api_key=key)
		
		try:
			## Trying the old access token
			f = open('at.txt', 'r') 
			access_token = f.read();
			f.close();

			#initiating kite
			self.kite.set_access_token(access_token)
		except:	
			##Requesting user to get the new request token
			print('Please open this url in browser and copy the request_token from the redirected url.')
			print(login_url)
			request_token = str(input("Paste the request token here:"))
			data = self.kite.generate_session(request_token, api_secret=secret)
			access_token = data['access_token']
			#initiating kite
			self.kite.set_access_token(access_token)

			f = open('at.txt', 'w') 
			f.write(access_token); 
			f.close();

	def get(self):
		return self.kite;
#whenever a trading advise is published kite will execute it
