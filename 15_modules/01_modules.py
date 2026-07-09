# Python provides built-in and third-party modules.
# Two type of modules in python:
# 1. Build in Modules : https://docs.python.org/3/py-modindex.html : list of all build-in modules
# 2. External Modules


import math
import os
import mymodule
# Installing External Libraries with pip
import requests

print(math.sqrt(16))
mymodule.hello()
r = requests.get("https://www.google.com")
print(r.text)