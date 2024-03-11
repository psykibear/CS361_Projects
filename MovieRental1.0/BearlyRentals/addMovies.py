import json
from tkinter import *


def submit(name, location, genre):
    with open('stock.json', 'r') as infile:
        movies = json.load(infile)
    status = "On Shelf at " + location
    movies['number'] += 1
    index = movies['number']
    movies['member'][index] = {'name': name,
                              'location': location,
                              'status': status,
                              'genre': genre}
    with open('stock.json', 'w') as outfile:
        json.dump(movies, outfile, indent=4)

    update = Tk()
    update.title("System Message")
    update.geometry("240x160")

    message = "\nSystem updated successfully!\nmovie: " +\
              name + "\nis No. " + str(index) + " in the system.\n"
    mess = Label(update, text=message, font=('roboto', 15))
    mess.grid(row=0, column=0, padx=20)
    close = Button(update, text="Close this window",
                   command=update.destroy,
                   font=('roboto', 18))
    close.grid(row=1, column=0, padx=20, pady=10,
               ipadx=25, ipady=10)
    update.mainloop()


def addMovie():
    root = Tk()
    root.title("Add a movie")
    root.geometry("750x550")
    genre = ["Action and Adventure", "Animation", "Comedy", "Crime", "Documentary", "Drama"
           "Fantasy", "Horror", "Romance", "Science Fiction", "Thriller", "Western"]

    category = StringVar(root)
    category.set("Please make a selection from below categories")

    # Label
    welcome = Label(root, text="Add a movie to Bearly Rentals",
                    font=('roboto', 40), anchor=CENTER)
    welcome.grid(row=0, column=0, columnspan=3, padx=45,
                 pady=20)
    nameLabel = Label(root, text="Please type in the movie's name:",
                      font=('roboto', 18), anchor=CENTER)
    nameLabel.grid(row=1, column=1, pady=20)
    locationLabel = Label(root, text="What's the location of this movie?",
                          font=('roboto', 18), anchor=CENTER)
    locationLabel.grid(row=2, column=1, pady=20)
    categoryLabel = Label(root, text="Which category is this movie?",
                          font=('roboto', 18), anchor=CENTER)
    categoryLabel.grid(row=3, column=1, pady=20)

    # text box
    name = Entry(root, width=40)
    name.grid(row=1, column=2)
    location = Entry(root, width=40)
    location.grid(row=2, column=2)
    genreBox = OptionMenu(root, category, *genre)
    genreBox.grid(row=3, column=2)

    # button
    submitB = Button(root, text="SUBMIT",
                     command=lambda: submit(name.get(),
                                            location.get(),
                                            genre.get()),
                     font=('roboto', 18))
    submitB.grid(row=4, column=0, columnspan=3,
                 pady=10, ipadx=90, ipady=20)

    terminate = Button(root, text="Close This Window", command=root.destroy,
                       font=('roboto', 36))
    terminate.grid(row=5, column=0, columnspan=3,
                   pady=10, ipadx=90, ipady=20)
    root.mainloop()
