#!/usr/bin/python

_test = None

def get_test():
  global _test
  return _test

def set_test(var):
  global _test
  _test = var
