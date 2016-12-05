#coding: utf-8
from collections import defaultdict

def matchToDict(matchobj):
  d = defaultdict(list)
  for k, v in matchobj:
    d[k].append(v)
  return d

