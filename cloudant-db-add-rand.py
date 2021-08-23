#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import os
import sys
import random

from cloudant.client import Cloudant
from cloudant.error import CloudantException
from cloudant.result import Result, ResultByKey

# 環境変数から定義すること
serviceUsername = os.environ['IBM_USER']
servicePassword = os.environ['IBM_PASS']
serviceURL = os.environ['IBM_URL']


# DBに接続する
client = Cloudant(serviceUsername, servicePassword, url=serviceURL)
client.connect()
myDB_kano = client.create_database("first-db")

# 新しいドキュメントを作成する
objToday = datetime.datetime.today()
strTemp = str(objToday.year) + str(objToday.month) + str(objToday.day) + str(objToday.hour) + str(objToday.minute)
strRand = random.random()
jsonDocument = {
    "_id": ":".join(("docid", strTemp)),
    "table": 'job',
    "comment": strRand
}
newDocument = myDB_kano.create_document(jsonDocument)


