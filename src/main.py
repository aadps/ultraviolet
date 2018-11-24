#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""Main loop of UltraViolet."""

import config
import mailer
import data
import time

time.sleep(5)  # wait 5 secs for datebase to come online
data.initData()
