#!/usr/bin/env python3
# lib/debug.py

from models.__init__ import CONN, CURSOR
from models.movie import Movie
from models.actor import Actor
from helpers import (list_movies_ass_one_actor)


import ipdb

def reset_database():
    Movie.drop_table()
    Actor.drop_table()
   
    Movie.create_table()
    Actor.create_table()
  

    actor=Actor.create("Tom Hanks",60)
    actor=Actor.create("Meryl Streep",70)
    movie=Movie.create("Forrest Gump",1994,2)
    movie=Movie.create("The Post",2017,1)

    list_movies_ass_one_actor()
  
    

reset_database()
ipdb.set_trace()
