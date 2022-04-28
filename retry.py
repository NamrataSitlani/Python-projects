import requests
from requests.packages.urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter
from urllib3.exceptions import MaxRetryError


s = requests.Session()

retries = Retry(total=5,
                backoff_factor=1,
                status_forcelist=[ 500, 502, 503, 504 ]
                )

s.mount('http://', HTTPAdapter(max_retries=retries))
try:
    s.get("https://www.google.com/")
    print("Hi")
except MaxRetryError:
    raise
