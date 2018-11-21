#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""Main loop of UltraViolet."""

import config
import mailer

mailer.sendLetter(config.TEST_CONFIG['receiver'], "Romans",
                  config.TEST_CONFIG['subject'])
