import socket
import getreadings
import flask
from gevent.pywsgi import WSGIServer

app = flask.Flask(__name__)
#app.config["DEBUG"] = True
app.config["HOST"] = '0.0.0.0'

@app.route('/',methods=['GET'])
def home():
        return "{}".format(socket.gethostname())

@app.route('/api/v1/temp',methods=['GET'])
def api_temp():
        readings = getreadings.get_sensor_readings()
        return readings

if __name__ == '__main__':
        http_server = WSGIServer(('',5000),app)
        http_server.serve_forever()
