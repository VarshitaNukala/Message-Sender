# importing the client from the twilio
from twilio.rest import Client
# Account Sid
account_sid = 'ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
#Account token
auth_token = 'token'
# instantiating the Client
client = Client(account_sid, auth_token)
# sending message
message = client.messages.create(body='Hi there! How are you?', from_=+1123456789
, to=+15558478530)
# printing sid to verify that the message has been sent successfully
print(message.sid)
