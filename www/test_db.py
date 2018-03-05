#! /usr/bin/env python3
#-*- coding:utf-8 -*-

import asyncio
import orm

from models import User, Blog, Comment

loop = asyncio.get_event_loop()

async def testInsert():
    await orm.create_pool(loop=loop, host='127.0.0.1', port=3306,user='root', password='root', db='py3_web1_app_db')

    u = User(name='test', email='test@example.com', passwd='123456', image='about:blank')

    await u.save()

loop.run_until_complete(testInsert())