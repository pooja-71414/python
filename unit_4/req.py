import requests

data=requests.get('https://github.com/pooja-71414')
# print(data)  # give output in response state -states code
# print(data.text)  # give output in text state -states code
file=open('pooja.jpg','wb')
file.write(data.content)