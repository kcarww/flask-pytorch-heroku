import requests

response = requests.post('http://localhost:5000/predict',
                         files={'file': open('seven.jpg', 'rb')})
print(response.text)