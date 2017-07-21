Overview of GreenScreen control
===============================

A simple server to headlessly control a
`GreenScreen <http://greenscreen.io>`__ installation and a set of
Chromecasts. Controls the assignment of GreenScreen channels to
Chromecasts using the GreenScreen API, and then can start/stop casting
to a particular Chromecast.

Depends on a working `GreenScreen <http://greenscreen.io>`__
installation.

Starting the server
-------------------

::

    ./greenscreen_control.py $APPID

$APPID is the value of your "Applicakion ID" from the `Google Cast
Developer Console <https://cast.google.com/publish/>`__. This will have
been setup as part of the `GreenScreen <http://greenscreen.io>`__
installation.

Available arguments:

::

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

Protocol
--------

Uses a simple line-based protocol to a TCP server (default port: 4995):

Assign the "CCTV" channel to the "Kitchen" chromecast, and start casting
it:

::

    chromecast=Kitchen,channel=CCTV,cast=1

Assign the "CCTV" channel to the "Kitchen" chromecast, don't cast it
(either prepares for future casting, or assumes already casted):

::

    chromecast=Kitchen,channel=CCTV

Cast the currently assigned channel (whatever that is):

::

    chromecast=Kitchen,cast=1

Stop casting:

::

    chromecast=Kitchen,cast=0
