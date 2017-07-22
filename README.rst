Overview of GreenScreen control
===============================

A simple module, command line utility and tcp server to headlessly control a
`GreenScreen <http://greenscreen.io>`_ installation and a set of
Chromecasts. Controls the assignment of GreenScreen channels to
Chromecasts using the GreenScreen API, and then can start/stop casting
to a particular Chromecast.

Requires a working `GreenScreen <http://greenscreen.io>`_ installation.

AppID
-----

In these instructions, $APPID is the value of your "Application ID" from the
`Google Cast Developer Console <https://cast.google.com/publish/>`_. This will
have been setup as part of the `GreenScreen <http://greenscreen.io>`_
installation.

Using the command line utility
------------------------------

Set the CCTV channel on the Kitchen Chromecast:

::

    $ greenscreen_control -c CCTV set-channel Kitchen

Start casting a given AppID on a Chromecast:

::

    $ greenscreen_control -a $APPID cast Kitchen

Stop casting on the Kitchen Chromecast:

::

    $ greenscreen_control stop-cast Kitchen

Available arguments:

::

    usage: greenscreen_control [-h] [-g GREENSCREEN_SERVER] [-a APPID]
                               [-c CHANNEL] [-l {ERROR,WARNING,INFO,DEBUG}]
                               {set-channel,cast,stop-cast} chromecast

    positional arguments:
      {set-channel,cast,stop-cast}
                            Command
      chromecast            Chromecast name

    optional arguments:
      -h, --help            show this help message and exit
      -g GREENSCREEN_SERVER, --greenscreen_server GREENSCREEN_SERVER
                            GreenScreen server:port
      -a APPID, --appid APPID
                            Chromecast Greenscreen App ID
      -c CHANNEL, --channel CHANNEL
                            GreenScreen channel to set
      -l {ERROR,WARNING,INFO,DEBUG}, --loglevel {ERROR,WARNING,INFO,DEBUG}
                        Logging level


Starting the server
-------------------

Start a simple TCP server (default port 4995) to control greenscreen and
Chromecast casting.

::

    $ greenscreen_control_server $APPID

Available arguments:

::

    usage: greenscreen_control_server [-h] [-g GREENSCREEN_SERVER] [-p PORT]
                                      [-l {ERROR,WARNING,INFO,DEBUG}]
                                      appid

    positional arguments:
      appid                 Chromecast Greenscreen App ID

    optional arguments:
      -h, --help            show this help message and exit
      -g GREENSCREEN_SERVER, --greenscreen_server GREENSCREEN_SERVER
                            GreenScreen server:port
      -p PORT, --port PORT  TCP server port number
      -l {ERROR,WARNING,INFO,DEBUG}, --loglevel {ERROR,WARNING,INFO,DEBUG}
                            Logging level


Server Protocol
---------------

The TCP server uses a simple line-based protocol, easily controlled from
scripts, cron or home automation.

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
