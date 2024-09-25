# # download html page
# import requests
# data=requests.get('https://github.com/pooja-71414')
# file=open('req_html.html','wb')
# file.write(data.content)
# file.close()

# download pdf
import requests
data=requests.get('')
file=open('req_pdf.pdf','wb')
file.write(data.content)
file.close()

# # download image
# import requests
# data=requests.get('')
# file=open('req_jpg.png','wb')
# file.write(data.content)
# file.close()