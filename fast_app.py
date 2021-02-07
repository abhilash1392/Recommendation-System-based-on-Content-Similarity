# Importing the libraries 
import uvicorn 
from fastapi import FastAPI 
from cosinesimilarity import recommend_movies


app = FastAPI()



@app.get('/')
def welcome():
	return {'Welcome':'Recommended movies using content similarity'}


@app.post('/{movie_name}')
def get_recommend_movies(movie_name:str):
	answer = recommend_movies(movie_name)

	return {'The recommended movies are:':answer}



if __name__=="__maine__":
	uvicorn.run(app)


# uvicorn fast_app:app --reload