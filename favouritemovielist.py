favourite_movies = []

def create_movie():
    title = input("Enter movie name to add: ").strip()
    if title:
        favourite_movies.append(title)
        print(f"Movie '{title}' added.")
    else:
        print("Movie name cannot be empty.")

def read_movies():
    if not favourite_movies:
        print("Your movie list is empty.")
    else:
        print("\n Your Favorite Movies:")
        for i, movie in enumerate(favourite_movies, 1):
            print(f"{i}. {movie}")
        print()

def update_movie():
    read_movies()
    try:
        index = int(input("Enter the movie number to update: ")) - 1
        if 0 <= index < len(favourite_movies):
            new_title = input("Enter new movie name: ").strip()
            if new_title:
                old_title = favourite_movies[index]
                favourite_movies[index] = new_title
                print(f"Updated '{old_title}' to '{new_title}'.")
            else:
                print("New movie name cannot be empty.")
        else:
            print("Invalid movie number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_movie():
    read_movies()
    try:
        index = int(input("Enter the movie number to delete: ")) - 1
        if 0 <= index < len(favourite_movies):
            removed = favourite_movies.pop(index)
            print(f"Deleted '{removed}' from your list.")
        else:
            print("Invalid movie number.")
    except ValueError:
        print("Please enter a valid number.")

def show_menu():
    print("""
===== Favorite Movie List Manager =====
1. Add Movie
2. Show All Movies
3. Update Movie
4. Delete Movie
5. Exit
""")

def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-5): ").strip()
        if choice == '1':
            create_movie()
        elif choice == '2':
            read_movies()
        elif choice == '3':
            update_movie()
        elif choice == '4':
            delete_movie()
        elif choice == '5':
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
