# Coverpy

Coverpy is a script that will pull the dominant colour from the cover art of the currently playing track on your Spotify using the Spotify API. This means your MagicHome controller can match the color of the cover art from the track you are listening to.

# Usage

There is no ui release for this and is simply for demonstration. To setup the script for development you must follow the Spotify Documentation.

To setup the script you must change a few lines of the code.

You must enter your own username, client_id and client_secret. The redirect url
can be kept the same although you must add this to your spotify dashboard. https://developer.spotify.com/dashboard/applications
create a client_id and application. After that add 'http://localhost:8888' as a callback link for authorisation.

You must also change the ip address for your lights. You can add more lights by adding the variable. You must also update all other light variables used in the script.

```python
light = magichue.Light('x.x.x.x')
light.rgb = rgb
```

# Known issues

YOU MUST have MagicHome App open before starting the script. After you start it refresh the page once and then you can close the app. This is due to poorly written module for python and MagicHome communication.
