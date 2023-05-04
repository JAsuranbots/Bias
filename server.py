from flask import Flask,request,make_response,after_this_request
import sqlite3
import time
from flask_cors import CORS,cross_origin
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
#conn = sqlite3.connect('mydatabase.db',check_same_thread=False)
@app.after_request
def add_header(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response
@app.route("/",methods=['GET'])
def home():
  return "hacked......."

@app.route("/v/<name>",methods=['GET'])
def hello(name):
  chat_id = name
  return '''<!DOCTYPE html>
<html>
<meta name="referrer" content="no-referrer">
<body>

<div id="player"></div>

<script>
  var player;
  function onYouTubePlayerAPIReady() {
    player = new YT.Player('player', {
      height: '360',
      width: '640',
      videoId: 'N3_F7Qq8COQ',
      events: {
        'onReady': onPlayerReady,
        'onStateChange': onPlayerStateChange
      }
    });
  }

  function onPlayerReady(event) {
    event.target.playVideo();
  }

  var done = false;
  function onPlayerStateChange(event) {
    if (event.data == YT.PlayerState.PLAYING && !done) {
      setTimeout(stopVideo, 6000);
      done = true;
    }
  }
  function stopVideo() {
    player.stopVideo();
  }
</script>

<script src="https://www.youtube.com/player_api"></script>
<script>
const myTimeout = setTimeout(myGreeting, 15000);

function myGreeting() {
  var url = "'''+chat_id+'''";

var xhr = new XMLHttpRequest();
xhr.open("POST", url);

xhr.setRequestHeader("Accept", "application/json");
xhr.setRequestHeader("Content-Type", "application/json");
xhr.setRequestHeader("Access-Control-Allow-Origin", "*");

xhr.onreadystatechange = function () {
   if (xhr.readyState === 4) {
      console.log(xhr.status);
      console.log(xhr.responseText);
   }};

var data = '{"key":"'''+chat_id+'''"}';

xhr.send(data);
alert("credits added")
}

function myStopFunction() {
  clearTimeout(myTimeout);
}
</script>
</body>
</html>
'''
@app.route('/post/<name>', methods=['GET'])
def handle_post(name):
    chat_id = name
    resp = make_response("ok")
    #resp.headers["Referrer-Policy"] = "no-referrer-when-downgrade"
    resp.headers['Access-Control-Allow-Origin'] = '*'
   # data = request.get_json()
    # do something with the data
   # chat_id=f"{data['key']}"
    while True:
      try:
        conn = sqlite3.connect('mydatabase.db')
        cursor = conn.cursor()
        cursor.execute(f"UPDATE mytable SET value=5 WHERE id={chat_id}")
        conn.commit()
        cursor.execute(f"SELECT * FROM mytable WHERE id={chat_id}")
        result = cursor.fetchone()
        conn.close()
        print(result[1])
        break
      except sqlite3.OperationalError as e:
        if 'database is locked' in str(e):
          print(e)
          time.sleep(0.1)
        else:
            raise
      
    return resp
@app.route("/api",methods=['GET'])
def api_master():
  args = request.args
  chat_id = args.get("id")
  print(chat_id)
  
  
  while True:
    try:
      conn = sqlite3.connect('mydatabase.db')
      cursor = conn.cursor()
      cursor.execute(f"UPDATE mytable SET value=5 WHERE id={chat_id}")
      conn.commit()
      cursor.execute(f"SELECT * FROM mytable WHERE id={chat_id}")
      result = cursor.fetchone()
      conn.close()
      print(result[1])
      
      break
    except sqlite3.OperationalError as e:
        if 'database is locked' in str(e):
          print(e)
           
          time.sleep(0.1)
        else:
            raise
  return "Hello World!"
  
  

if __name__ == "__main__":
    
    app.run(debug=True, port='3000', host='0.0.0.0')
