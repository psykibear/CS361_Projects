import json
import tkinter as tk
from tkinter import messagebox


def load_movies(filename='stock.json'):
    """Load movies from a JSON file, return empty dict if not found."""
    try:
        with open(filename, 'r') as infile:
            return json.load(infile)
    except FileNotFoundError:
        return {'number': 0, 'member': {}}


def save_movies(movies, filename='stock.json'):
    """Save movies to a JSON file."""
    with open(filename, 'w') as outfile:
        json.dump(movies, outfile, indent=4)


def update_stock(name, location, category):
    """Updates the movie stock information."""
    movies = load_movies()
    index = movies['number'] + 1
    movies['member'][index] = {
        'name': name,
        'location': location,
        'status': "On Shelf at " + location,
        'category': category
    }
    movies['number'] = index
    save_movies(movies)
    return index


def show_update_message(index, name):
    """Displays a message indicating the system was updated."""
    messagebox.showinfo("System Message", f"System updated successfully!\nMovie: {name}\nis No. {index} in the system.")


class MovieAdderGUI:
    """GUI for adding a new movie."""

    def __init__(self, root):
        self.root = root
        root.title("Add a Movie")
        root.geometry("960x600")

        categories = ["Action and Adventure", "Animation", "Comedy", "Crime", "Drama", "SciFi and Fantasy", "Horror",
                      "Thriller"]
        self.category_var = tk.StringVar(value=categories[0])  # Default value

        tk.Label(root, text="Welcome to Bearly Rentals", font=('roboto', 24)).grid(row=0, columnspan=2, padx=10,
                                                                                   pady=10)
        tk.Label(root, text="Please type in the movie's name:", font=('roboto', 14)).grid(row=1, sticky=tk.W, padx=10)
        tk.Label(root, text="What's the location of this movie based on the movie's genre? "
                            "Action and Adventure=M1, Animation=M2, Comedy=M3, "
                            "Crime=M4, Drama=M5, SciFi and Fantasy=M6, Horror=M7, Thriller=M8",
                            font=('roboto', 14)).grid(row=2, sticky=tk.W, padx=10)
        tk.Label(root, text="Which category is this movie?", font=('roboto', 14)).grid(row=3, sticky=tk.W, padx=10)

        self.name_entry = tk.Entry(root)
        self.name_entry.grid(row=1, column=1, padx=10, pady=5)
        self.location_entry = tk.Entry(root)
        self.location_entry.grid(row=2, column=1, padx=10, pady=5)
        tk.OptionMenu(root, self.category_var, *categories).grid(row=3, column=1, padx=10, pady=5)

        tk.Button(root, text="SUBMIT", command=self.submit).grid(row=4, columnspan=2, pady=10)
        tk.Button(root, text="Close This Window", command=root.destroy).grid(row=5, columnspan=2, pady=10)

    def submit(self):
        """Handles the submission of a new movie."""
        name = self.name_entry.get()
        location = self.location_entry.get()
        category = self.category_var.get()
        index = update_stock(name, location, category)
        show_update_message(index, name)


if __name__ == "__main__":
    root = tk.Tk()
    app = MovieAdderGUI(root)
    root.mainloop()
