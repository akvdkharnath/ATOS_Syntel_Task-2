import requests
from database import engine
from base_model import Base, Session
from movies import Movie as MovieModel


def main():
    url = "https://movie-database-imdb-alternative.p.rapidapi.com/"
    querystring = {"s":"Avengers","r":"json","page":"1"}
    headers = {
        'x-rapidapi-host': "movie-database-imdb-alternative.p.rapidapi.com",
        'x-rapidapi-key': "4c0789f539mshd20dd05df3dfe15p18f99ejsncb41c231e624"
        }
    response = requests.request("GET", url, headers=headers, params=querystring)

    data = response.json()
    movies_list = data.get("Search", [])
    db = Session()
    for i in movies_list:
        insert = MovieModel(**i)
        db.add(insert)
        print(i)
    db.commit()
        
if __name__ == "__main__":
    Base.metadata.create_all(engine)
    main()
