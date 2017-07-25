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

    usage: greenscreen_control_cli.py [-h] [-g GREENSCREEN_SERVER] [-a APPID]
                                      [-c CHANNEL] [-l {ERROR,WARNING,INFO,DEBUG}]
                                      [-r TRIES] [-t TIMEOUT] [-w RETRY_WAIT]
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
      -r TRIES, --tries TRIES
                            Chromecast connection tries. Default is infinite.
      -t TIMEOUT, --timeout TIMEOUT
                            Chromecast socket timeout seconds. Default is 30.
      -w RETRY_WAIT, --retry_wait RETRY_WAIT
                            Seconds to wait between Chromecast retries. Default is
                            5.


Starting the server
-------------------

Start a simple TCP server (default port 4995) to control greenscreen and
Chromecast casting.

::

    $ greenscreen_control_server -l INFO -a $APPID

Available arguments:

::

    usage: greenscreen_control_server.py [-h] [-g GREENSCREEN_SERVER] [-a APPID]
                                         [-c CHANNEL]
                                         [-l {ERROR,WARNING,INFO,DEBUG}]
                                         [-r TRIES] [-t TIMEOUT] [-w RETRY_WAIT]
                                         [-p PORT]

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
      -r TRIES, --tries TRIES
                            Chromecast connection tries. Default is infinite.
      -t TIMEOUT, --timeout TIMEOUT
                            Chromecast socket timeout seconds. Default is 30.
      -w RETRY_WAIT, --retry_wait RETRY_WAIT
                            Seconds to wait between Chromecast retries. Default is
                            5.
      -p PORT, --port PORT  TCP server port number


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

Starting the server by default
------------------------------

Use the included greenscreen_control.service to start the server as a systemd
unit.
