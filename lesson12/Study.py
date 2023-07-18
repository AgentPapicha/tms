import time

import requests

start = time.perf_counter()
resp = requests.get("http://yandex.com")
print(time.perf_counter()-start)
print(resp)