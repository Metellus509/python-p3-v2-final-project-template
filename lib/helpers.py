# lib/helpers.py
from models.movie import Movie
from models.actor import Actor



def exit_program():
    print("Goodbye!")
    exit()

def list_movies():
    movies = Movie.get_all()
    for movie in movies:
        print(movie)

def find_movie_by_name():
    name = input("Enter movie name: ")
    movie = Movie.find_by_name(name)
    if movie:
        print(movie)
    else:
        print("Movie not found.")

def find_movie_by_id():
    id = int(input("Enter movie ID: "))
    movie = Movie.find_by_id(id)
    if movie:
        print(movie)
    else:
        print("Movie not found.")

def create_movie():
    name = input("Enter movie name: ")
    year = int(input("Enter movie year: "))
    actor_id=int(input("Enter actor ID: "))
    try :
        movie = Movie.create(name, year,actor_id)
        print(f"Created movie: {movie}")
    except Exception as exc:
        print("Error creating movie:",{exc})

def update_movie():
    id = int(input("Enter movie ID to update: "))
    movie = Movie.find_by_id(id)
    if movie:
        name = input(f"Enter new name (current: {movie.name}): ") 
        prod_year = input(f"Enter new year (current: {movie.prod_year}): ") 
        actor_id = input(f"Enter new actor_id (current: {movie.actor_id}): ")
        try:
            movie.name = name
            movie.prod_year = int(prod_year)
            movie.actor_id = int(actor_id)
            movie.update()
            print(f"Updated movie: {movie}")
        except Exception as exc:
            print("Error updating movie:",{exc})
    else:
        print("Movie not found.")

def delete_movie():
    id = int(input("Enter movie ID to delete: "))
    movie = Movie.find_by_id(id)
    if movie:
        movie.delete()
        print(f"Movie deleted:{id}")
    else:
        print(f"Movie not found:{id}")

def list_actors():
    actors = Actor.get_all()
    for actor in actors:
        print(actor)

def find_actor_by_name():
    name = input("Enter actor name: ")
    actor = Actor.find_by_name(name)
    if actor:
        print(actor)
    else:
        print(f"Actor not found:{name}")

def find_actor_by_id():
    id = int(input("Enter actor ID: "))
    actor = Actor.find_by_id(id)
    if actor:
        print(actor)
    else:
        print(f"Actor not found:{id}")

def create_actor():
    name = input("Enter actor name: ")
    age = int(input("Enter actor age: "))
    try:
        actor = Actor.create(name, age)
        print(f"Created actor: {actor}")
    except Exception as exc:
        print("Error creating actor:",{exc})

def update_actor():
    id = int(input("Enter actor ID to update: "))
    actor = Actor.find_by_id(id)
    if actor:
        name = input(f"Enter new name (current: {actor.name}): ") 
        age = input(f"Enter new age (current: {actor.age}): ") 
        try:
            actor.name = name
            actor.age = int(age)
            actor.update()
            print(f"Updated actor: {actor}")
        except Exception as exc:
            print("Error updating actor:",{exc})
    else:
        print(f"Actor not found:{id}")

def delete_actor():
    id = int(input("Enter actor ID to delete: "))
    actor = Actor.find_by_id(id)
    if actor:
        actor.delete()
        print(f"Actor deleted:{id}")
    else:
        print(f"Actor not found:{id}")


def list_movies_ass_one_actor():
    id_ = input("Enter actor id: ")
    actor = Actor.find_by_id(id_)
    if actor :
        try:
            movies = actor.movies()
            for mov in movies:
                print(mov)
        except Exception as exc:
            print("Error listing movies:", exc)
    else:
        print("Actor doesn't exist")