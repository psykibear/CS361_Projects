import json
from tkinter import Tk, Label, Entry, Button


def display_message(message):
    """Displays a message window with the operation result."""
    update = Tk()
    update.title("System Message")
    update.geometry("240x160")
    Label(update, text=message, font=('roboto', 15)).grid(row=0, column=0, padx=20)
    Button(update, text="Close this window", command=update.destroy, font=('roboto', 18)).grid(row=1, column=0,
                                                                                               padx=20, pady=10,
                                                                                               ipadx=25, ipady=10)


class MovieReturnApp:
    def __init__(self, stock_file='stock.json'):
        self.stock_file = stock_file
        self.root = Tk()
        self.setup_gui()

    def load_movies(self):
        """Loads the movie data from the stock file."""
        with open(self.stock_file, 'r') as infile:
            return json.load(infile)

    def save_movies(self, movies):
        """Saves the modified movie data back to the stock file."""
        with open(self.stock_file, 'w') as outfile:
            json.dump(movies, outfile, indent=4)

    def return_movie(self, index, location):
        """Processes the return of a movie."""
        movies = self.load_movies()
        if index in movies['member']:
            if movies['member'][index]['status'] == 'movie rented':
                movies['member'][index]['location'] = location
                movies['member'][index]['status'] = "On Shelf at " + location
                self.save_movies(movies)
                message = "\nmovie returned successfully!\nmovie status updated.\n"
            else:
                message = "\nSystem info mismatched.\nPlease contact employee.\n"
        else:
            message = "\nINVALID INPUT\nThe index does not exist."
        display_message(message)

    def setup_gui(self):
        """Sets up the GUI for returning a movie."""
        self.root.title("Return a movie")
        self.root.geometry("480x300")

        Label(self.root, text="Please type in the movie's index: ", font=('roboto', 18), anchor='center').grid(row=0,
                                                                                                               column=0,
                                                                                                               padx=40,
                                                                                                               pady=20)
        Label(self.root, text="Where do you put it?", font=('roboto', 18), anchor='center').grid(row=1, column=0,
                                                                                                 padx=40, pady=20)
        index_entry = Entry(self.root, width=10)
        index_entry.grid(row=0, column=1)
        location_entry = Entry(self.root, width=10)
        location_entry.grid(row=1, column=1)

        Button(self.root, text="SUBMIT", command=lambda: self.return_movie(index_entry.get(), location_entry.get()),
               font=('roboto', 18)).grid(row=2, column=1, pady=10, ipadx=20, ipady=10)
        Button(self.root, text="Close This Window", command=self.root.destroy, font=('roboto', 24)).grid(row=3,
                                                                                                         column=0,
                                                                                                         columnspan=2,
                                                                                                         pady=10,
                                                                                                         ipadx=20,
                                                                                                         ipady=10)

    def run(self):
        """Runs the main application loop."""
        self.root.mainloop()


if __name__ == '__main__':
    app = MovieReturnApp()
    app.run()
