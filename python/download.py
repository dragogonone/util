#!/usr/bin/env python
# webからhtmlをダウンロードしてきて保存する
# option save = trueにすると即保存
# option save = falseにすると中身をテキストで返す


# coding: utf-8
import sys
import os
import shutil
import requests

def download(url, save=False):
    file_name = os.path.basename(url)
    res = requests.get(url, stream=True)
    if res.status_code == 200:
      res.encoding = res.apparent_encoding
      if save:
        with open(file_name, 'w') as f:
          f.write(res.text)
        print("completed download")
      else:
        return res.text
    else:
      print("status code is {}".format(res.status_code))


def save_image(url, path="./"):
    if path[-1:] != '/':
        path += '/'
    res = requests.get(url, stream=True)
    if res.status_code == 200:
        filename = url.split('/')[-1].split('?')[0]

        #pathを作成
        if not os.path.exists(path):
            os.mkdir(path)
        # saveData というバイナリデータを作成
        saveData = open(path + filename, 'wb');

        # saveDataに取得した画像を書き込み
        saveData.write(res.content);
        saveData.close()
 
if __name__ == "__main__":
  if len(sys.argv) < 1:
    print("usage: python download.py filename")
    exit(0)
  url = sys.argv[1]
  download(url, save=True)

