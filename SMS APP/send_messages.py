# from email import message
# from http import client
from twilio.rest import Client
from credentials import account_sid, auth_token, my_twilio_phone, my_cell_phone

client = Client(account_sid,auth_token)

my_message = 'Hello'
message = client.messages.create(to=my_cell_phone,from_ = my_twilio_phone, body = my_message)


