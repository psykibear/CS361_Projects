import json
from tkinter import Tk


class MovieLibrary:
    def __init__(self, stock_file='stock.json'):
        self.stock_file = stock_file
        self.categories = {
            '1': "Action and Adventure",
            '2': "Animation",
            '3': "Comedy",
            '4': "Crime",
            '5': "Drama",
            '6': "SciFi and Fantasy",
            '7': "Horror",
            '8': "Thriller"
        }

    def load_movies(self):
        try:
            with open(self.stock_file, 'r') as infile:
                return json.load(infile)
        except FileNotFoundError:
            return {'member': {}, 'number': 0}

    def save_movies(self, movies):
        with open(self.stock_file, 'w') as outfile:
            json.dump(movies, outfile, indent=4)

    def list_by_category(self):
        category_index = input("PLEASE TYPE IN ONE OF THE ABOVE INDICES (1 - 8): ")
        category_name = self.categories.get(category_index)
        if not category_name:
            print("INVALID INPUT\n")
            return
        print(f"For {category_name} category, we have:")
        movies = self.load_movies()
        for index, movie in movies['member'].items():
            if movie['category'] == category_name:
                print(f"\t{index}. {movie['name']}\n\t----{movie['status']}")

    def update_movie(self, action):
        movies = self.load_movies()
        index = input("\nType in the movie index or 0 to cancel: ")
        if index == '0':
            return
        movie = movies['member'].get(index)
        if not movie:
            print("\nINVALID INPUT\nThe index number does not exist.")
            return self.update_movie(action)

        if action == 'rent':
            if movie['status'] == 'movie rented':
                print("\nI am sorry, the movie is currently rented by other people.\n")
            elif movie['status'] == 'DELETED':
                print("\nI am sorry, the movie is no longer available.\n")
            else:
                movie['status'] = 'movie rented'
                print("\nYou successfully rented the movie.\nmovie status updated.\n")
        elif action == 'return':
            if movie['status'] == 'movie rented':
                movie['location'] = input("\nPlease tell me the location where you put the movie:\n")
                movie['status'] = "On Shelf at " + movie['location']
                print("\nYou successfully returned the movie.\nmovie status updated.\n")
            else:
                print("\nThe movie was not rented.\n")
        elif action == 'delete':
            finalCheck = input("\nAre you sure you want to delete it? Type in Y/N here: ")
            if finalCheck.upper() == 'Y':
                movie['status'] = 'DELETED'
                print("\nYou successfully deleted the movie.\nmovie status updated.\n")
            else:
                print("\nDeletion cancelled.\n")
        self.save_movies(movies)

    def add_movie(self):
        movies = self.load_movies()
        name = input("\nPlease type in the movie's name:\n")
        location = input("What's the location of this movie?\n")
        cat = input("Which category is this movie?\n")
        index = movies['number'] + 1
        movies['member'][str(index)] = {
            'name': name,
            'location': location,
            'status': "On Shelf at " + location,
            'category': cat
        }
        movies['number'] = index
        self.save_movies(movies)
        print(f"\nSystem updated successfully! Movie {name} is No. {index} in the system.\n")

    def perform_action(self, action):
        if action in ['rent', 'return', 'delete']:
            self.update_movie(action)
            if input(f"\nDo you want to {action} another movie? Please type in Y/N: ").upper() == 'Y':
                self.perform_action(action)


def __init__(self):
    self.root = Tk()
    self.root.title("Bearly Rentals")
    self.movie_library = MovieLibrary()  # Create an instance of MovieLibrary
    self.run_app()
    self.movie_library.add_movie()
    self.movie_library.perform_action('rent')
    self.movie_library.perform_action('return')
    self.movie_library.perform_action('delete')


if __name__ == "__main__":
    MovieLibrary()
