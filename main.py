import sys
import spotipy
import spotipy.util as util
from PIL import Image
import requests
from io import BytesIO
import magichue
import time
import numpy as np
import scipy
import scipy.misc
import scipy.cluster

username = 'liams212'
client_id = 'YOUR_CLIENT_ID'
client_secret= 'YOUR_CLIENT_SECRET'
redirect_uri = 'http://localhost:8888'

light = magichue.Light('YOUR_CONTROLLER_IP')
light1 = magichue.Light('YOUR_CONTROLLER_IP')

NUM_CLUSTERS = 5
nrgb = []
art = []
rgb = []


scope = 'user-read-currently-playing'

def average_colour(img):
    nrgb = []
    rgb = []
    ar = np.asarray(img)
    shape = ar.shape
    ar = ar.reshape(scipy.product(shape[:2]), shape[2]).astype(float)

    codes, dist = scipy.cluster.vq.kmeans(ar, NUM_CLUSTERS)

    vecs, dist = scipy.cluster.vq.vq(ar, codes)         # assign codes
    counts, bins = scipy.histogram(vecs, len(codes))    # count occurrences

    index_max = scipy.argmax(counts)                    # find most frequent
    peak = codes[index_max]

    for i in peak:
        x = round(i, 0)
        rgb.append(int(x))
    print(rgb)
    r = rgb[0]
    g = rgb[1]
    b = rgb[2]

    if r > g and r > b:
        div = 225 / r
        ng = g * div
        nb = b * div
        nrgb.append(225)
        nrgb.append(round(int(ng), 0))
        nrgb.append(round(int(nb), 0))
        lights(nrgb)
    if g > r and g > b:
        div = 225 / g
        nr = r * div
        nb = b * div
        nrgb.append(round(int(nr), 0))
        nrgb.append(225)
        nrgb.append(round(int(nb), 0))
        lights(nrgb)
    if b > r and b > g:
        div = 225 / b
        nr = r * div
        ng = g * div
        nrgb.append(round(int(nr), 0))
        nrgb.append(round(int(ng), 0))
        nrgb.append(225)
        lights(nrgb)
    else:
        print("FATAL ERROR")


def main():
    art = []
    token = util.prompt_for_user_token(username,scope,client_id,client_secret,redirect_uri)
    sp = spotipy.Spotify(auth=token)
    results = sp.current_user_playing_track()
    if results == None:
        print('ERROR: No song is being played')
        time.sleep(5)
        main()

    image = results['item']['album']['images']
    for x in image:
        art.append(x['url'])


    print(art[0])
    response = requests.get(art[0])
    img = Image.open(BytesIO(response.content))
    print (img.size) #debugging
    img = img.resize((300, 300)) #Can be resized for better optimization not needed
    average_color = average_colour(img)


def lights(nrgb):

    print(nrgb)
    if light.on or light1.on == False:
        light.on = True
        light1.on = True

    light.rgb = (nrgb)
    light1.rgb = (nrgb)

    time.sleep(5)

    #Resets the arrays to be used again

while True:
    main()
