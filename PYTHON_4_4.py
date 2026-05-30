#!/usr/bin/env python3

import requests
URL = 'https://httpbin.org/post'
URL_GET = 'https://httpbin.org/get'


data = {
    'username': 'prueba_shelsye',
    'password': 'sena1234',
    'email': 'pruebashelsye@soy.sena.com'
}
response_get = requests.get(URL_GET, params=data)
print(response_get.text[:300])


response_post = requests.post(URL, data=data)
print(dict(response_post.headers))
print("\nCódigo de estado:", response_post.status_code)

cd ~/Python_VSCode
git add PYTHON_4_4.py
git commit -m "Ejercicio 4_4 resuelto - GET y POST"
git push origin main