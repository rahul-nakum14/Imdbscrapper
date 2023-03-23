import requests
from bs4 import BeautifulSoup

class Imdb:
    def __init__(self,rating=None) :
        self.url = 'https://www.imdb.com/chart/toptv'
        self.rating = rating 

    def main(self):
        response  = requests.get(self.url)

        soup = BeautifulSoup(response .text,'html.parser')

        title = soup.find_all('td',class_="titleColumn")

        rating = soup.find_all('td',class_="ratingColumn imdbRating")

        # for t,r in zip(title,rating):
        #     if float(r.find('strong').text) >self.rating:
        #         # print(t.find('a').text,"-->",r.find('strong').text)
        #         pass

        #     else:
        #         print(t.find('a').text,"-->",r.find('strong').text)

        for t, r in zip(title, rating):
            rating_value = float(r.find('strong').text)
            if self.rating is None :
                print(f"{t.find('a').text} --> {rating_value}")
            else:
                if float(r.find('strong').text) >self.rating:
                        print(t.find('a').text,"-->",r.find('strong').text)

            


if __name__ == "__main__":
    rating = input("Enter Rating (Press Enter to print all): ")
    if rating:
        obj = Imdb(float(rating))
    else:
        obj = Imdb()
    obj.main()


            # if self.rating is None or rating_value > self.rating:
