import socket
from twilio.rest import Client

def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]

account_sid = "AC61781473c67d12f6c479d410f23d9238"
auth_token = "d6509b7a46aff0fbcf68e8e820471ad8"
my_name = socket.gethostname()
my_ip = get_ip_address()

client = Client(account_sid, auth_token)

message = client.messages.create( to="+17072666211", from_="+13345092632", body="Good morning!  My name is {} and I live at {}".format(my_name, my_ip))