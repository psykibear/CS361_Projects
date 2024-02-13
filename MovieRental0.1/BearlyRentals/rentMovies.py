import json
from tkinter import Tk, Label, Entry, Button


def update_movie_status(index, status):
    """Update the status of a movie in the stock."""
    try:
        with open('stock.json', 'r') as infile:
            movies = json.load(infile)

        if index in movies['member']:
            movies['member'][index]['status'] = status
            with open('stock.json', 'w') as outfile:
                json.dump(movies, outfile, indent=4)
            return True
        else:
            return False
    except Exception as e:
        print(f"Error updating movie status: {e}")
        return False


def display_message(message):
    """Display a system message."""
    update = Tk()
    update.title("System Message")
    update.geometry("240x160")
    Label(update, text=message, font=('roboto', 15)).grid(row=0, column=0, padx=20)
    Button(update, text="Close this window", command=update.destroy, font=('roboto', 18)).grid(row=1, column=0, padx=20,
                                                                                               pady=10, ipadx=25,
                                                                                               ipady=10)
    update.mainloop()


def rent(index):
    """Handle the borrowing of a movie."""
    try:
        with open('stock.json', 'r') as infile:
            movies = json.load(infile)

        if index in movies['member']:
            current_status = movies['member'][index]['status']
            if current_status == 'movie rented':
                message = "\nI am sorry.\nThe movie is currently rented by another user.\n"
            elif current_status == 'DELETED':
                message = "\nI am sorry.\nThe movie is no longer available.\n"
            else:
                if update_movie_status(index, 'movie Borrowed'):
                    message = "\nmovie successfully rented!\nmovie status updated.\n"
                else:
                    message = "\nError updating movie status.\n"
        else:
            message = "\nINVALID INPUT\nThe index number does not exist.\n"
    except Exception as e:
        message = f"\nAn error occurred: {e}\n"

    display_message(message)


def rent_movie_gui():
    """GUI for renting a movie."""
    root = Tk()
    root.title("Borrow a movie")
    root.geometry("480x300")
    Label(root, text="Please type in the movie's index:", font=('roboto', 18), anchor='center').grid(row=0, column=0,
                                                                                                     padx=40, pady=40)
    index_entry = Entry(root, width=10)
    index_entry.grid(row=0, column=1)
    Button(root, text="SUBMIT", command=lambda: rent(index_entry.get()), font=('roboto', 18)).grid(row=1, column=1,
                                                                                                     pady=10, ipadx=20,
                                                                                                     ipady=10)
    Button(root, text="Close This Window", command=root.destroy, font=('roboto', 24)).grid(row=2, column=0,
                                                                                           columnspan=2, pady=10,
                                                                                           ipadx=20, ipady=10)
    root.mainloop()


if __name__ == "__main__":
    rent_movie_gui()
