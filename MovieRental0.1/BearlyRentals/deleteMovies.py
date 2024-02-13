import json
from tkinter import Tk, Label, Button, Entry


def display_message(message):
    update = Tk()
    update.title("System Message")
    update.geometry("240x160")
    Label(update, text=message, font=('roboto', 15)).grid(row=0, column=0, padx=20)
    Button(update, text="Close this window", command=update.destroy, font=('roboto', 18)).grid(row=1, column=0,
                                                                                               padx=20, pady=10,
                                                                                               ipadx=25, ipady=10)
    update.mainloop()


class MovieManager:
    def __init__(self, stock_file='stock.json'):
        self.stock_file = stock_file
        self.root = Tk()

    def load_movies(self):
        try:
            with open(self.stock_file, 'r') as infile:
                return json.load(infile)
        except FileNotFoundError:
            return {'member': {}}

    def save_movies(self, movies):
        with open(self.stock_file, 'w') as outfile:
            json.dump(movies, outfile, indent=4)

    def delete_movie(self, index):
        movies = self.load_movies()

        if index in movies['member']:
            if movies['member'][index]['status'] == 'DELETED':
                message = "\nThe movie's status is already deleted in the system.\n"
            else:
                movies['member'][index]['status'] = 'DELETED'
                self.save_movies(movies)
                message = "\nYou successfully deleted the movie. Movie status updated.\n"
        else:
            message = "\nINVALID INPUT\nThe index number does not exist.\n"

        display_message(message)

    def confirm_deletion(self, index):
        term = Tk()
        term.title("Delete?")
        term.geometry("360x160")
        Label(term, text="Are you sure to delete it?", font=('roboto', 24), anchor='center').grid(row=0, column=0,
                                                                                                  columnspan=2, padx=45,
                                                                                                  pady=20)
        Button(term, text="Yes", command=lambda: self.delete_movie(index), font=('roboto', 18)).grid(row=1, column=0,
                                                                                                     pady=10, ipadx=25,
                                                                                                     ipady=10)
        Button(term, text="No", command=term.destroy, font=('roboto', 18)).grid(row=1, column=1, pady=10, ipadx=25,
                                                                                ipady=10)
        term.mainloop()

    def delete_movie_gui(self):
        self.root.title("Delete a movie")
        self.root.geometry("480x300")
        Label(self.root, text="Please type in the movie's index:", font=('roboto', 18), anchor='center').grid(row=0,
                                                                                                              column=0,
                                                                                                              padx=40,
                                                                                                              pady=40)
        index_entry = Entry(self.root, width=10)
        index_entry.grid(row=0, column=1)
        Button(self.root, text="SUBMIT", command=lambda: self.confirm_deletion(index_entry.get()),
               font=('roboto', 18)).grid(row=1, column=1, pady=10, ipadx=20, ipady=10)
        Button(self.root, text="Close This Window", command=self.root.destroy, font=('roboto', 24)).grid(row=2,
                                                                                                         column=0,
                                                                                                         columnspan=2,
                                                                                                         pady=10,
                                                                                                         ipadx=20,
                                                                                                         ipady=10)
        self.root.mainloop()


if __name__ == "__main__":
    manager = MovieManager()
    manager.delete_movie_gui()
