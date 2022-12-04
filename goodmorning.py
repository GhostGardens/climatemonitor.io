import socket
from twilio.rest import Client

def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]

account_sid = "{account SID}"
auth_token = "{auth token}"
my_name = socket.gethostname()
my_ip = get_ip_address()

client = Client(account_sid, auth_token)

message = client.messages.create( to="{receiver number}", from_="{twilio sender number}", body="Good morning!  My name is {} and I live at {}".format(my_name, my_ip))
