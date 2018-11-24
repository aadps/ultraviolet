#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""Data persistence layer of UltraViolet."""

import mysql.connector

import config

SPIDER_PREFIX = 'spi_'  # prefix of tables related to a spider
uvDB = None


def initData():
    """
    Connect to database and initialize primary tables.

    :returns: nothing.
    """
    global uvDB
    uvDB = mysql.connector.connect(host=config.DB_CONFIG['host'],
                                   user=config.DB_CONFIG['user'])
    cursor = uvDB.cursor()
    cursor.execute('CREATE DATABASE IF NOT EXISTS ultraviolet;')
    cursor.execute('USE ultraviolet;')

    # ts1 < ts2 < ts3, ts1 - create, ts2 - track, ts3 - respond
    cursor.execute('CREATE TABLE IF NOT EXISTS person (ID INT AUTO_INCREMENT, '
                   + 'email VARCHAR(100) NOT NULL, '
                   + 'response TEXT, '
                   + 'category INT NOT NULL, '
                   + 'letter INT NOT NULL, '
                   + 'spider INT NOT NULL, '
                   + 'view INT NOT NULL DEFAULT 0, '
                   + 'city TEXT, '
                   + 'lat DECIMAL(10, 8), '
                   + 'lng DECIMAL(11, 8), '
                   + 'ts1 TIMESTAMP DEFAULT CURRENT_TIMESTAMP, '
                   + 'ts2 TIMESTAMP, '
                   + 'ts3 TIMESTAMP, '
                   + 'PRIMARY KEY(ID), UNIQUE KEY(email));')
    cursor.execute('CREATE TABLE IF NOT EXISTS signature '
                   + '(ID INT AUTO_INCREMENT, '
                   + 'email VARCHAR(100) NOT NULL, '
                   + 'signature TEXT, '
                   + 'PRIMARY KEY(ID), UNIQUE(email));')
    cursor.execute('CREATE TABLE IF NOT EXISTS category '
                   + '(ID INT AUTO_INCREMENT, '
                   + 'category TEXT, '
                   + 'PRIMARY KEY(ID));')
    cursor.execute('CREATE TABLE IF NOT EXISTS letter '
                   + '(ID INT AUTO_INCREMENT, '
                   + 'letter TEXT, '
                   + 'PRIMARY KEY(ID));')
    cursor.execute('CREATE TABLE IF NOT EXISTS spider '
                   + '(ID INT AUTO_INCREMENT, '
                   + 'spider TEXT, '
                   + 'PRIMARY KEY(ID));')


def registerData(name, type):
    """
    Register new category, letter, or spider (and create its tables).

    :param name: The name of the item to be registered.
    :param type: 0 for category, 1 for letter, 2 for spider.
    :returns: nothing.
    """
    global uvDB


def insertURL(spider, url):
    """
    Insert a url into spider's url table.

    :param spider: The name of the spider.
    :param url: The url to be inserted.
    :returns: nothing.
    """
    global uvDB


def selectURL(spider):
    """
    Acquire an unscanned url from spider's url table and change its status.

    :param spider: The name of the spider.
    :returns: An unscanned url.
    """
    global uvDB


def insertPerson(spider, person):
    """
    Insert a person into spider's person table.

    :param spider: The name of the spider.
    :param person: The person to be inserted.
    :returns: nothing.
    """
    global uvDB


def updatePerson(spider, person):
    """
    Update a person in spider's person table.

    :param spider: The name of the spider.
    :param person: The person to be updated.
    :returns: nothing.
    """
    global uvDB


def promotePerson(spider):
    """
    Promote a person to primary person table.

    :param spider: The name of the spider.
    :returns: The person to be promoted.
    """
    global uvDB


def updatePrimaryPerson(person, signature):
    """
    Update a person in primary person table (along with signature).

    :param person: The person to be updated.
    :param person: The signature to be inserted.
    :returns: nothing.
    """
    global uvDB
