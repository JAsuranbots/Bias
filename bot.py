from telethon import TelegramClient, events
import re
import asyncio
from telethon.tl.custom import Button
import PyBypass as bypasser
import requests
import json
import sqlite3
client = TelegramClient('anonn56ne2',1651836,"f8244276a17b5b2a711e7501857c8e55")
url_regex = re.compile(r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+')
check_subscribe = []
def callback(current, total):
    global pbar
    global prev_curr
    pbar.update(current-prev_curr)
    prev_curr = current
def youtube_subscribe(chat_id):
  conn = sqlite3.connect('youtube2.db')
  cursor = conn.cursor()
  cursor.execute('''CREATE TABLE IF NOT EXISTS mytable (id  TEXT)''')
  #cursor.execute('SELECT id FROM mytable ORDER BY id DESC LIMIT 1')
  ##last_value = cursor.fetchone()[0]
  #print(last_value)
  api_key = 'AIzaSyAQbEi082RXAQyXditWY5cCL-cjYTMQc9M'
  youtube = build('youtube', 'v3', developerKey=api_key)
  channel_id = 'UCrknCDE8hTnuYEBKgR84KVg'
  channel_response = youtube.channels().list(part='statistics',id=channel_id).execute()
  subscriber_count = channel_response['items'][0]['statistics']['subscriberCount']
  print(subscriber_count)
  cursor.execute(f"INSERT INTO mytable VALUES ({subscriber_count})")
  conn.close()
  #subscriber count---------------
  conn = sqlite3.connect('youtube.db')
  cursor = conn.cursor()
  cursor.execute('''CREATE TABLE IF NOT EXISTS mytable (id  TEXT, value  TEXT,)''')
  cursor.execute(f"SELECT COUNT(*) FROM mytable WHERE id ={chat_id}")
  count = cursor.fetchone()[0]
  conn.close
  if count > 0:
    print("id exist")
  else:
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO mytable VALUES ({chat_id},0)")
    conn.commit()
    conn.close


@client.on(events.CallbackQuery)
async def handle_url_button(event):
    url = event.data
    await client.send_message('https://'+url)
@client.on(events.NewMessage(pattern='(?i).*/credit'))
async def handler(event):
  chat_id = event.chat_id
  conn = sqlite3.connect('mydatabase.db')
  cursor = conn.cursor()
  cursor.execute(f"SELECT * FROM mytable WHERE id={chat_id}")
  result = cursor.fetchone()
  print(result)
  conn.close()
  await client.send_message(chat_id,f"{result[1]} credits remaining ")
@client.on(events.NewMessage(pattern='(?i).*/start'))
async def handler(event):
  chat_id = event.chat_id
  await client.send_message(chat_id,"join must to use me !!! ",buttons=[[Button.url('support youtube channel', 'https://www.youtube.com/@Infinitrocyber'),Button.url('join telegram channel!', 'https://t.me/infinitrocyberlegend')],[Button.url('help', 'https://t.me/+4i9gfXvGcBA2ZTFl')]]
      )
  
@client.on(events.NewMessage())
async def handler(event):
  dir(event)
 # prev_curr = 0
 # print(event)
  #pbar = tqdm(total=1, unit='B', unit_scale=True)
  links =event
  #await client.send_message(chat,"🌠 downloading 🌠")
  key = "509061uc94uwe1gl6aqq"
  chat_id = event.chat_id
  a = requests.get(f"https://pdisk.pro/api/upload/server?key={key}").json()
  sess_id = a["sess_id"]
  print(a)
  result = a["result"]
  await client.send_message(chat_id,"please wait.....")  
  print(result)
  path = await client.download_media(event.media)
  print(path)
  files = {
    'sess_id': (None, f'{sess_id}'),
    'utype': (None, 'prem'),
    'file_0': open(f'{path}', 'rb'),
}
  response = requests.post(f'{result}', files=files).json()
  c = response
  c_json = json.dumps(str(c))
  f = json.loads(c_json)
  m= f.replace("{","").replace("}","").replace("[","").replace("]","").replace("'","")
  cm_json = m.split("file_code")[1].split(",")[0].replace(":","")
  print(f)
  print(cm_json)
  print("ok...file")
  vbc = f"https://pdisk.pro/{cm_json}"
  #pbar.close()
  await client.send_message(chat_id,vbc.replace(" ",""))
  #bypassed_link = bypasser.bypass(event.raw_text)
  #await event.reply(bypassed_link)
print("bor_starting......")
client.start(bot_token="5939463789:AAGXWKRX7w7uCXS-BREv_XiJ1ib5GjOa9bA")
print("bot_run_until_con......")
client.run_until_disconnected()
