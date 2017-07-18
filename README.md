# Overview of GreenScreen control

A simple server to headlessly control a [greenscreen.io](GreenScreen) installation and a set of Chromecasts. Controls the assignment of GreenScreen channels to Chromecasts using the GreenScreen API, and then can start/stop casting to a particular Chromecast.

Depends on a working [greenscreen.io](GreenScreen) installation.

## Starting the server

```
./greenscreen_control.py $APPID
```

$APPID is the value of your "Application ID" from the [https://cast.google.com/publish/#/overview](Google Cast Developer Console). This will have been setup as part of the [greenscreen.io](GreenScreen) installation.

Available arguments:
```
usage: greenscreen_control.py [-h] [-g GREENSCREEN_SERVER] [-p PORT]
                              [-l {ERROR,WARNING,INFO,DEBUG}]
                              appid

positional arguments:
  appid                 Chromecast Greenscreen App ID

optional arguments:
  -h, --help            show this help message and exit
  -g GREENSCREEN_SERVER, --greenscreen_server GREENSCREEN_SERVER
                        GreenScreen server:port
  -p PORT, --port PORT  tcp server port number
  -l {ERROR,WARNING,INFO,DEBUG}, --loglevel {ERROR,WARNING,INFO,DEBUG}
                        logging level
```

## Protocol

Uses a simple line-based protocol to a TCP server (default port: 4995):

Assign the "CCTV" channel to the "Kitchen" chromecast, and start casting it:
```
chromecast=Kitchen,channel=CCTV,cast=1
```

Assign the "CCTV" channel to the "Kitchen" chromecast, don't cast it (either prepares for future casting, or assumes already casted):
```
chromecast=Kitchen,channel=CCTV
```

Cast the currently assigned channel (whatever that is):
```
chromecast=Kitchen,cast=1
```

Stop casting:
```
chromecast=Kitchen,cast=0
```
