from telethon import TelegramClient, events
import re
#from tqdm import tqdm
import asyncio
from telethon.tl.custom import Button
import os
import requests
import json
import sqlite3
from bot_keys import a,b,c,pdisk

client = TelegramClient('sd2',a,b)
url_regex = re.compile(r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+')
check_subscribe = []
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
  print(event)
  links =event
  key = pdisk
  chat_id = event.chat_id
  a = requests.get(f"https://pdisk.pro/api/upload/server?key={key}").json()
  sess_id = a["sess_id"]
  print(a)
  result = a["result"]
  try:
    await client.send_message(chat_id,"please wait.....")  
    print(result)
    path = await client.download_media(event.media)
    print(path)
    files = {'sess_id': (None, f'{sess_id}'),'utype': (None, 'prem'),'file_0': open(f'{path}', 'rb'),}
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
    os.remove(path)
  except:
    print("went wrong.....")

print("bor_starting......")
client.start(bot_token=c)
print("bot_run_until_con......")
client.run_until_disconnected()
