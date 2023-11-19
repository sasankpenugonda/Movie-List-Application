import json

file_name = "movie_records.json"

def load_movies():
    try:
        with open(file_name, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_movies(movies):
    with open(file_name, 'w') as file:
        json.dump(movies, file, indent=4)

def show_all_movies(movies):
    if not movies:
        print("No movies found. Add some movies by clicking 2 at the Main Menu")
        return
    for movie in movies:
        print(f"{movie['name']}")

def show_and_choose_movie(movies):
    if not movies:
        print("No movies found.")
        return
    
    print("\nMovies List:")
    for idx, movie in enumerate(movies, start=1):
        print(f"{idx}. {movie['name']}")

    choice = input("\nEnter the number of the movie to see details: ")

    try:
        choice = int(choice)
        if 1 <= choice <= len(movies):
            chosen_movie = movies[choice - 1]
            print("\nChosen Movie Details:")
            print(f"Title: {chosen_movie['name']}")
            print(f"Director: {chosen_movie['director']}")
            print(f"Release Year: {chosen_movie['release_year']}")
            print(f"Language: {chosen_movie['language']}")
            print(f"Rating: {chosen_movie['rating']}")
        else:
            print("Invalid movie number. Please select a valid option.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def add_new_movie(movies):
    name = input("Enter movie name: ")
    director = input("Enter director's name: ")
    release_year = input("Enter release year: ")
    language = input("Enter language: ")
    rating = input("Enter rating: ")

    movie = {
        'name': name,
        'director': director,
        'release_year': release_year,
        'language': language,
        'rating': rating
    }
    movies.append(movie)
    save_movies(movies)
    print("Movie added successfully.")

def filter_movies(movies):
    print("\nFilter Options:")
    print("1. Filter by Name")
    print("2. Filter by Director")
    print("3. Filter by Release Year")
    print("4. Filter by Language")
    print("5. Filter by Rating")
    choice = input("Enter your choice: ")

    filtered_movies = []

    if choice == '1':
        search_term = input("Enter movie name to filter: ")
        filtered_movies = [movie for movie in movies if search_term.lower() == movie['name'].lower()]
    elif choice == '2':
        search_term = input("Enter director's name to filter: ")
        filtered_movies = [movie for movie in movies if search_term.lower() == movie['director'].lower()]
    elif choice == '3':
        search_term = input("Enter release year to filter: ")
        filtered_movies = [movie for movie in movies if search_term == movie['release_year']]
    elif choice == '4':
        search_term = input("Enter language to filter: ")
        filtered_movies = [movie for movie in movies if search_term.lower() == movie['language'].lower()]
    elif choice == '5':
        search_term = input("Enter rating to filter: ")
        filtered_movies = [movie for movie in movies if search_term == movie['rating']]
    else:
        print("Invalid choice. No movies filtered.")

    if filtered_movies:
        print(f"\nFiltered Movies based on criteria:")
        show_all_movies(filtered_movies)
    else:
        print("No movies found matching the criteria.")

def search_movie(movies):
    print("\nSearch Options:")
    print("1. Search by Movie Name")
    print("2. Search by Director")
    print("3. Search by Release Year")
    print("4. Search by Language")
    print("5. Search by Rating")
    choice = input("Enter your choice: ")

    found_movies = []

    if choice == '1':
        search_term = input("Enter movie name to search: ")
        found_movies = [movie for movie in movies if search_term.lower() in movie['name'].lower()]
    elif choice == '2':
        search_term = input("Enter director's name to search: ")
        found_movies = [movie for movie in movies if search_term.lower() in movie['director'].lower()]
    elif choice == '3':
        search_term = input("Enter release year to search: ")
        found_movies = [movie for movie in movies if search_term == movie['release_year']]
    elif choice == '4':
        search_term = input("Enter language to search: ")
        found_movies = [movie for movie in movies if search_term.lower() in movie['language'].lower()]
    elif choice == '5':
        search_term = input("Enter rating to search: ")
        found_movies = [movie for movie in movies if search_term == movie['rating']]
    else:
        print("Invalid choice. No movies found.")

    if found_movies:
        print(f"\nFound {len(found_movies)} movie(s) matching the search:")
        show_all_movies(found_movies)
    else:
        print("No movie found.")

def update_movie(movies):
    print("\nUpdate Options:")
    print("1. Update by Name")
    print("2. Update by Director")
    print("3. Update by Release Year")
    print("4. Update by Language")
    print("5. Update by Rating")
    choice = input("Enter your choice: ")

    if choice == '1':
        search_term = input("Enter movie name to update: ")
        for movie in movies:
            if search_term.lower() in movie['name'].lower():
                new_name = input("Enter new name: ")
                movie['name'] = new_name
                print("Movie name updated successfully.")
                save_movies(movies)
                return
    elif choice == '2':
        search_term = input("Enter movie name to update director: ")
        for movie in movies:
            if search_term.lower() in movie['name'].lower():
                new_director = input("Enter new director: ")
                movie['director'] = new_director
                print("Director updated successfully.")
                save_movies(movies)
                return
    elif choice == '3':
        search_term = input("Enter movie name to update release year: ")
        for movie in movies:
            if search_term.lower() in movie['name'].lower():
                new_release_year = input("Enter new release year: ")
                movie['release_year'] = new_release_year
                print("Release year updated successfully.")
                save_movies(movies)
                return
    elif choice == '4':
        search_term = input("Enter movie name to update language: ")
        for movie in movies:
            if search_term.lower() in movie['name'].lower():
                new_language = input("Enter new language: ")
                movie['language'] = new_language
                print("Language updated successfully.")
                save_movies(movies)
                return
    elif choice == '5':
        search_term = input("Enter movie name to update rating: ")
        for movie in movies:
            if search_term.lower() in movie['name'].lower():
                new_rating = input("Enter new rating: ")
                movie['rating'] = new_rating
                print("Rating updated successfully.")
                save_movies(movies)
                return
    else:
        print("Invalid choice. Movie details not updated.")

def delete_movie(movies):
    movie_to_delete = input("Enter the name of the movie to delete: ")
    found = False

    for movie in movies:
        if movie['name'].lower() == movie_to_delete.lower():
            cf=input(f"Are you sure to delete Movie '{movie_to_delete}'. Confirm Yes with'Y' or No with 'N': ")
            if cf.lower()=='y':
                movies.remove(movie)
                found = True
                print(f"Movie '{movie_to_delete}' deleted successfully.")
                save_movies(movies)
                break
            else:
                found = True
                print("Good decision")
                break

    if not found:
        print(f"Movie '{movie_to_delete}' not found in the records. No changes made.")


def get_movies_in_language(movies):
    unique_languages = set(movie['language'] for movie in movies)

    print("\nAvailable Languages:")
    for index, language in enumerate(unique_languages, start=1):
        print(f"{index}. {language}")
    
    choice = input("Enter the number of the language to get the count of movies: ")
    
    try:
        selected_language = list(unique_languages)[int(choice) - 1]
        count = sum(1 for movie in movies if movie['language'].lower() == selected_language.lower())
        print(f"Number of movies in {selected_language}: {count}")
    except (ValueError, IndexError):
        print("Invalid selection. Please choose a valid language option.")


def main():
    movies = load_movies()
    while True:
        print("\n===== Movie List Application =====")
        print("\n===== Main Menu =====")
        print("1. Show all Movies")
        print("2. Show a Movie record")
        print("3. Add a New Movie")
        print("4. Filter Movies based on criteria")
        print("5. Search for a Movie")
        print("6. Update a Movie's Details")
        print("7. Delete a Movie")
        print("8. Get number of movies count in a specified language")
        print("9. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            show_all_movies(movies)
        elif choice == '2':
            show_and_choose_movie(movies)
        elif choice == '3':
            add_new_movie(movies)
        elif choice == '4':
            filter_movies(movies)
        elif choice == '5':
            search_movie(movies)
        elif choice == '6':
            update_movie(movies)
        elif choice == '7':
            delete_movie(movies)
        elif choice == '8':
            get_movies_in_language(movies)
        elif choice == '9':
            print("Exiting the Movie List Application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()