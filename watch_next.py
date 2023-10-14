import spacy

nlp = spacy.load('en_core_web_md')
from decimal import *

#create a function to return which movies a user would watch next if they have watched Planet Hulk with the description “Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator.”
#e function should take in the description as a parameter and return the title of the most similar movie

def movie_to_watch(movie_description):
    #open the movies document
    movies = open('movies.txt', 'r')
    #I will spilt the movies and their descriptions
    the_descriptions_split = []

    for i in movies:
        the_descriptions_split.append(i.split(':'))

    #now i will get the number of movies in the text file
    amount = len(the_descriptions_split)
    
    #make a list to store the similarity values.
    similarities_list = []

    sentence = nlp(movie_description)

    #iterate over the text file
    for number in range(0, amount):
        #check similarities between the description of hulk movie and the other movie descriptions
        similarities_list.append(nlp(the_descriptions_split[number][1]).similarity(sentence))

    #now to get the movie with the highest similarity
    highest = max(similarities_list)
    #to get the index of the movie with the highest similarity
    highest_index = similarities_list.index(highest)

    #return the title of the movie that has the highest similarity.
    return the_descriptions_split[highest_index][0]

hulk_movie = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."

print("The movie that a user should watch after they have watch Hulk is" + movie_to_watch(hulk_movie))