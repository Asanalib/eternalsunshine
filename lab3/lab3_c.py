# Dictionary of movies

movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

#1
import random
movie = movies[random.randint(0, 14)]
value = movie["imdb"]
if value > 5.5:
    print ("True")
else:
    print ("False")

#2

def high (movies):
    for m in movies:
        if m["imdb"] > 5.5:
            return m
        
print (high(movies))

#3
def category(movies, category):
    for m in movies:
        if m["category"] == category:
            return m
print(category(movies, input()))

#4
def avg (movies):
    scores = []
    for m in movies:
        scores.append(m["imdb"])  
    avg = sum(scores) / len(scores)
    return avg 
    
print(avg(movies))


#5

def avg_cat (movies, category):
    category= []          
    for m in movies:
        if m["category"] == category:
            category.append(m)

    scores = []             
    for m in category:
        scores.append(m["imdb"])

    return sum(scores) / len(scores) 

print(avg_cat(movies, input()))
