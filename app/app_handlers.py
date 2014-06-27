#! /usr/bin/env python
# -*- coding: utf-8 -*-

from basehandler import basehandler
from google.appengine.ext import db

class AppHandler(basehandler.BaseHandler):
    def get(self):
        self.render('base.html')
