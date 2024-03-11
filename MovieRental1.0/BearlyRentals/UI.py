import tkinter as tk
from tkinter import messagebox

def browse_by_genre():
    messagebox.showinfo("Browse by Genre", "Functionality to browse by genre.")

def rent_movie():
    messagebox.showinfo("Rent a Movie", "Functionality to rent a movie.")

def return_movie():
    messagebox.showinfo("Return a Movie", "Functionality to return a movie.")

def add_movie():
    messagebox.showinfo("Add a Movie", "Functionality to add a movie to the catalog.")

def delete_movie():
    messagebox.showinfo("Delete a Movie", "Functionality to delete a movie from the catalog.")

def random_suggestion():
    messagebox.showinfo("Random Suggestion", "Functionality to get a random movie suggestion.")

def setup_ui(master):
    # Create the main menu
    main_menu = tk.Menu(master)
    master.config(menu=main_menu)

    # Create a Movie Menu
    movie_menu = tk.Menu(main_menu, tearoff=0)
    main_menu.add_cascade(label="Movies", menu=movie_menu)

    # Add options to the Movie Menu
    movie_menu.add_command(label="Browse by Genre", command=browse_by_genre)
    movie_menu.add_command(label="Rent a Movie", command=rent_movie)
    movie_menu.add_command(label="Return a Movie", command=return_movie)
    movie_menu.add_separator()
    movie_menu.add_command(label="Add a Movie to Catalog", command=add_movie)
    movie_menu.add_command(label="Delete a Movie from Catalog", command=delete_movie)

    # Create a Recommendation Menu
    recommendation_menu = tk.Menu(main_menu, tearoff=0)
    main_menu.add_cascade(label="Recommendation", menu=recommendation_menu)

    # Add options to the Recommendation Menu
    recommendation_menu.add_command(label="Random Suggestion", command=random_suggestion)

if __name__ == '__main__':
    root = tk.Tk()
    root.title("Bearly Rentals")
    root.geometry("400x300")  # Adjust the window size as needed

    setup_ui(root)

    root.mainloop()
