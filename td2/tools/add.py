#!/usr/bin/python
from stegano import slsb
secret = slsb.hide("suricate.png", "<!--havexY21kLmV4ZQo=havex-->>")
secret.save("suricate-2.png")
