This is a short python script that will pull the average colour from a spotify cover art using the api and a simple function.
The program will then inform LED controllers over wifi of the chosen RGB Colour.

Known issues:
IMPORTANT: YOU MUST have MagicHome App open before starting the script. After you start it refresh the page once and thern you can close the app.
The appropriate colour is only selected around 70% of the time needs major improvement

Change log

Minor improvements to colour selection

To setup the script you must change a few lines of the code.

On line 29 - 32 You must enter your own username, client_id and client_secret. The redirect url
can be kept the same although you must add this to your spotify dashboard. https://developer.spotify.com/dashboard/applications
create a client_id and application. After that add 'http://localhost:8888' as a callback link for authorisation.

You must also change the ip address for your lights. You can add more lights by adding the variable "lightx = magichue.Light('x.x.x.x')
and the scrolling down to line 97 adding "lightx.on = True" and then underneath add "lightx.rgb = (rgb)"

Now you are ready to start the script the last step is IMPORTANT. For the lights to operate smoothly you must open the app then run the main.py script and refresh the app.
After this you can close the app as the script should be running smoothly without hang or delay.
# coverpy
