import sys
import os
import magichue
import time
import spotipy
import spotipy.util as util
from dotenv import load_dotenv
from colorthief import ColorThief
import urllib.request
import io

load_dotenv('env_file.env')

controller_1 = os.getenv("CONTROLLER_1")
controller_2 = os.getenv("CONTROLLER_2")

username = 'Liam212'
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
redirect_uri = 'http://localhost:8888/callback'

light = magichue.Light(controller_1)
light1 = magichue.Light(controller_2)

light.on = True
light1.on = True

rgb = []
prevSong = "null"
scope = 'user-read-currently-playing'

print("Fetching current playback...")

def dominant_color_from_url(url, tmp_file='tmp.jpg'):
    urllib.request.urlretrieve(url, tmp_file)
    color_thief = ColorThief(tmp_file)
    dominant_color = color_thief.get_color(quality=1)
    os.remove(tmp_file)
    return dominant_color

def main():
    results = getCurrentTrack()
    songName = results['item']['album']['name']
    albumArt = results['item']['album']['images'][0]['url'] 
    rgb = dominant_color_from_url(albumArt)
    lights(rgb, songName)
    

def lights(rgb, songName):
    if light.rgb == rgb:
        time.sleep(4)
    else:
        print("User is listening to",songName,"setting lights to average color")
        print("The lights have been set to the value of",rgb)
        light.rgb = (rgb)
        light1.rgb = (rgb)
        time.sleep(5)
        main()


def getCurrentTrack():
    token = util.prompt_for_user_token(username, scope, client_id, client_secret)

    if token:
        sp = spotipy.Spotify(auth=token)
        sp.trace = False
        results = sp.current_user_playing_track()
        return results
    else:
        print ("Can't get token for", username)

while True:
    main()