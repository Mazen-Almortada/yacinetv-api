import requests
import base64
import time
import os
import json
from dotenv import load_dotenv

load_dotenv()

class YacineTV:

  api_url = os.getenv("API_URL")
  key = os.getenv("API_KEY")

  def __init__(self):
    pass

  def decrypt(self, enc, key=key):
    enc = base64.b64decode(enc.encode("ascii")).decode("ascii")
    result = ""
    for i in range(len(enc)):
      result = result + chr(ord(enc[i]) ^ ord(key[i % len(key)]))
    return result

  def req(self, path):
    r = requests.get(self.api_url + path)
    timestamp = str(int(time.time()))
    if "t" in r.headers:
      timestamp = r.headers["t"]

    try:
      return json.loads(self.decrypt(r.text, key=self.key + timestamp))

    except Exception:
      return {
        "success": False,
        "error": "can't parse json."
      }

  def get_categories(self):
    return self.req("/api/categories")

  def get_category_channels(self, category_id):
    return self.req(f"/api/categories/{str(category_id)}/channels")

  def get_channel(self, channel_id):
    return self.req(f"/api/channel/{str(channel_id)}")

  def get_all_events(self):
    return self.req("/api/events")
  
  def get_event(self, event_id):
    return self.req(f"/api/event/{str(event_id)}")
  
  def search(self, query):
      return self.req(f"/api/search?query={query}")
