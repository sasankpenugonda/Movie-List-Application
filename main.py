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
        filtered_movies = [movie for movie in movies if search_term.lower() in movie['name'].lower()]
    elif choice == '2':
        search_term = input("Enter director's name to filter: ")
        filtered_movies = [movie for movie in movies if search_term.lower() in movie['director'].lower()]
    elif choice == '3':
        search_term = input("Enter release year to filter: ")
        filtered_movies = [movie for movie in movies if search_term == movie['release_year']]
    elif choice == '4':
        search_term = input("Enter language to filter: ")
        filtered_movies = [movie for movie in movies if search_term.lower() in movie['language'].lower()]
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


# Function for user-friendly movie search
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


# Function to update a movie's details
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

# Function to delete a movie
def delete_movie(movies):
    movie_to_delete = input("Enter the name of the movie to delete: ")
    found = False

    for movie in movies:
        if movie['name'].lower() == movie_to_delete.lower():
            cf=input(f"Are you sure. Do you want to delete Movie '{movie_to_delete}'. If yes enter 'Y' or enter 'N'")
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


# Function to get the number of movies in a specified language
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
        print("2. Add a New Movie")
        print("3. Filter Movies based on criteria")
        print("4. Search for a Movie")
        print("5. Update a Movie's Details")
        print("6. Delete a Movie")
        print("7. Get number of movies count in a specified language")
        print("8. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            show_all_movies(movies)
        elif choice == '2':
            add_new_movie(movies)
        elif choice == '3':
            filter_movies(movies)
        elif choice == '4':
            search_movie(movies)
        elif choice == '5':
            update_movie(movies)
        elif choice == '6':
            delete_movie(movies)
        elif choice == '7':
            count = get_movies_in_language(movies)
        elif choice == '8':
            print("Exiting the Movie List Application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
