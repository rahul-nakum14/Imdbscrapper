import requests
from bs4 import BeautifulSoup

class Imdb:
    def main(self):
        response  = requests.get('https://www.imdb.com/chart/toptv')
        soup = BeautifulSoup(response .text,'html.parser')

        title = soup.find_all('td',class_="titleColumn")

        rating = soup.find_all('td',class_="ratingColumn imdbRating")

        for t,r in zip(title,rating):
            print(t.find('a').text,"-->",r.find('strong').text)

if __name__ == "__main__":
    obj = Imdb()
    obj.main()

'''Greater than 8'''
# for t,r in zip(title,rating):
#     if float(r.find('strong').text) >8:
#         print(t.find('a').text,"-->",r.find('strong').text)
