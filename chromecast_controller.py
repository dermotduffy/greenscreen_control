#!/usr/bin/python

import logging
import pychromecast

class CachedChromecastController(object):
  def __init__(self):
    self._chromecasts = {}

  def discover_chromecasts(self):
    try:
      chromecasts = pychromecast.get_chromecasts_as_dict()
    except pychromecast.PyChromecastError:
      logging.exception("Could not discover Chromecasts")
      return

    if chromecasts:
      self._chromecasts = chromecasts

  def _get_chromecast(self, chromecast_name):
    if chromecast_name not in self._chromecasts:
      logging.error("Could not find Chromecast \"%s\"" % chromecast_name)
      return None
    else:
      return self._chromecasts[chromecast_name]
   
  def start_chromecast_app(self, chromecast_name, app_id):
    chromecast = self._get_chromecast(chromecast_name)
    if not chromecast:
      return False

    try:
      chromecast.wait()
      if chromecast.status:
        if chromecast.status.is_stand_by:
          chromecast.quit_app()
        logging.info("Starting app %s on Chromecast: %s" % (
            app_id, chromecast_name))
        chromecast.start_app(app_id)
        return True
    except pychromecast.PyChromecastError:
      logging.exception("Could not start app %s on Chromecast: %s" % (
          app_id, chromecast_name))
    return False

  def stop_chromecast_app(self, chromecast_name):
    chromecast = self._get_chromecast(chromecast_name)
    if not chromecast:
      return False

    try:
      chromecast.wait()
      if chromecast.status:
        logging.info("Stopping apps on Chromecast: %s" % chromecast_name)
        chromecast.quit_app()
        return True
    except pychromecast.PyChromecastError:
      logging.exception("Could not stop apps on Chromecast: %s" % (
          chromecast_name))
    
    return False
