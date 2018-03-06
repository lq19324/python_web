#! /usr/bin/env python3
#! -*- coding:utf-8 -*-

'url handlers'

import re, time, json, logging, hashlib, base64, asyncio

from coreweb import get, post

from models import User, Comment, Blog, next_id

import logging;logging.basicConfig(level=logging.INFO)


@get('/')
async def index(request):
    users = await User.findAll()
    logging.info('index user:%s' % users[0].email)
    return {
        '__template__':'test.html',
        'users':users
    }