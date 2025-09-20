# lib/cli.py

from helpers import (
    exit_program,
    list_movies,
    find_movie_by_name,
    find_movie_by_id,
    create_movie,
    update_movie,
    delete_movie,
    list_actors,
    find_actor_by_name,
    find_actor_by_id,
    create_actor,
    update_actor,
    delete_actor,
    list_movies_ass_one_actor
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            list_movies()
        elif choice == "2":
            find_movie_by_name()
        elif choice == "3":
            find_movie_by_id()
        elif choice == "4":
            create_movie()
        elif choice == "5":
            update_movie()
        elif choice == "6":
            delete_movie()
        elif choice == "7":
            list_actors()
        elif choice == "8":
            find_actor_by_name()
        elif choice == "9":
            find_actor_by_id()
        elif choice == "10":
            create_actor()
        elif choice == "11":
            update_actor()
        elif choice == "12":
            delete_actor()
        elif choice == "13":
            list_movies_ass_one_actor()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. List all movies")
    print("2. Find movie by name")
    print("3. Find movie by id")
    print("4: Create movie")
    print("5: Update movie")
    print("6: Delete movie")
    print("7. List all actors")
    print("8. Find actor by name")
    print("9. Find actor by id")
    print("10: Create actor")
    print("11: Update actor")
    print("12: Delete actor")
    print("13: Lister tous les movies d un acteur specifique")




if __name__ == "__main__":
    main()
