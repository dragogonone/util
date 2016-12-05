#!/usr/bin/env python
# unzipがない環境でunzipする

import sys
import zipfile

param = sys.argv

if len(param) < 1:
  print("usage: python unzip.py filename")
  exit(0)

filename = param[1]

if filename[-4:] != '.zip':
  print("file is not zip file")
  exit(0)

with zipfile.ZipFile(filename, "r") as z:
  z.extractall("./" + filename[:-4] + "/")
