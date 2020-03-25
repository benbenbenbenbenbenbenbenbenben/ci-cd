from flask import Flask, request
 
app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
   if request.method == 'GET':
      return '<h1>Hello from Webhook Listener App!</h1>'

if __name__ == "__main__":
    app.run()
