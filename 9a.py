import bs4 as beauty
import os
import requests
os.makedirs("test-comics",exist_ok=True)
starting_url="https://xkcd.com/"
count=13
for comic_number in range(count):
    image_url=f"{starting_url}{comic_number}/"
    image_data=requests.get(image_url)
    html_parser=beauty.BeautifulSoup(image_data.text,"html.parser")
    css_element=html_parser.select_one("#comic img")
    if(css_element):
        image_url="https:{}".format(css_element['src'])
        image_data=requests.get(image_url)
        print("Downloading ",image_url)
        with open("test-comics/comic{}.png".format(comic_number),"wb") as file:
            file.write(image_data.content)