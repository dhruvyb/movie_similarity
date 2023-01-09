planet_hulk_desc = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."

def movie_recommendation(movie_desc):
    import spacy

    # load similarity model
    nlp = spacy.load("en_core_web_md")

    # read movie text file to list variable 
    with open('movies.txt', 'r') as movie_file:
        movies = movie_file.readlines()

    # blank movie and similarity dictionaries
    movie_dict = {}


    # read each line and assign the movie label and description to a key and value in dictionary.
    for i in range(len(movies)):
        movie_list = movies[i].strip().split(':')
        movie_dict[movie_list[0].strip()] = movie_list[1]

    #nlp model on movie description
    model_desc = nlp(movie_desc)

    # base similarity and movie variable
    select_similarity = 0
    select_movie = ""

    # for loop to compare each movie description with movie description
    for j in movie_dict.keys():
        similarity = nlp(movie_dict[j]).similarity(model_desc)

        #if movie similarity, is greater than current selected movie similarity, then replace movie
        if similarity > select_similarity:
            select_similarity = similarity
            select_movie = j

    return select_movie

# passing planet hulk moview description to function and printing
print(movie_recommendation(planet_hulk_desc))