# Install and import the requests modules(is available) and use it to fetch data from "https://api.github.com/"

import requests

r = requests.get("https://api.github.com")
print(r.json())