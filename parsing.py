import requests
from bs4 import BeautifulSoup
import datetime

now = datetime.datetime.now()


page = 0

while True:
 
    url = ('https://www.kijiji.ca/b-apartments-condos/city-of-toronto/c37l1700273' + str(page))

    rock = requests.get(url)

    soup = BeautifulSoup(rock.text, "html.parser")

    teme = soup.find_all('div', class_='info')
    teme_image = soup.find_all('div', class_='image')

    title = []
    price = []
    date = []
    image = []
    page += 1


    
    for tem in teme:

        title = (tem.find('div', {'class':'title'}).text.strip())
        price = (tem.find('div', {'class':'price'}).text.strip())
        date = (tem.find('span', {'class': 'date-posted'}).text.strip())

    for te in teme_image:
        try:
            image = te.find('source').get('data-srcset')
        except AttributeError:
            image = 'None'


        if "/" not in date:
            date = now.strftime("%d/%m/%Y")
    
        
        print(f'Title: {title} \n')
        print(f'Price: {price} \n')
        print(date)
        print('\n'f'{image} \n')
        print(f'Page: {page} \n')
        


# image = product.find('div', {'class':'listbox_img'}).find('img').get('src')
