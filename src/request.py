import requests
import sys
from math import ceil

# URL
url = 'http://localhost:5000/'

arg = sys.argv[1]

r = requests.post(url, json={
    'exp': float(arg),
})

print(
    f'Salary for {float(arg)} year/s of experience should be ${ceil(round(r.json(), 2))}'
)