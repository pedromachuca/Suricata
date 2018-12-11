#!/usr/bin/python
from stegano import slsb

data = slsb.reveal("logs/files/file.1")
print data
