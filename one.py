import requests 
from bs4 import BeautifulSoup as bs 
import urllib.request

url = 'https://www.instagram.com'
username = input('Enter the Username: ')
response = requests.get(f"{url}/{username}/")

# Status Code either 200(OK Found URL) or 404(Not a valid URL)
response.status_code

#Printing the URL (will be printed only if staus_code responses to 200 or OK) 

finalurl = response.url
print(finalurl)
abc = requests.get(finalurl)
parseddata = bs(abc.text, "html.parser") 
catchimage = parseddata.find("meta",property="og:image")
cont = catchimage.attrs['content']

with open(username+'.jpg',"wb") as pic:
    binary=requests.get(cont).content
    pic.write(binary)
    