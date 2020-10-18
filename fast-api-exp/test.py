import requests,json

import base64
with open("ffff.jpg", "rb") as image_file:
    base64str = base64.b64encode(image_file.read()).decode("utf-8")

payload = json.dumps({
  "base64str": base64str,
  "threshold": 0.5
})
response = requests.put("http://127.0.0.1:8000/predict",data = payload)
data_dict = response.json()

print(data_dict)
