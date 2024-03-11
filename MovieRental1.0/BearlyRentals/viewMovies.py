import json
from tkinter import *


def view(genre):
    output = "For " + genre + " genre, we have:\n"
    with open('stock.json', 'r') as infile:
        movies = json.load(infile)
    for movie in movies['member']:
        if movies['member'][movie]['genre'] == genre:
            output += ('\t' + movie + '. ' + movies['member'][movie]['name'] + '\n\t----' +
                       movies['member'][movie]['status'] + '\n')
    root = Tk()
    root.title(genre)
    root.geometry("500x750")
    welcome = Label(root, text="Check out these!!!",
                    font=('roboto', 48), anchor=CENTER)
    welcome.grid(row=0, column=0, columnspan=3, padx=45,
                 pady=20)

    content = Label(root, text=output, font=('roboto', 18),
                    anchor='w', justify=CENTER)
    content.grid(row=2, column=0, columnspan=3, pady=10,
                 ipadx=25, ipady=20)

    terminate = Button(root, text="Close This Window", command=root.destroy,
                       font=('roboto', 24))
    terminate.grid(row=5, column=0, columnspan=3,
                   pady=10, ipadx=90, ipady=20)

    root.mainloop()


def listByGenre():
    root = Tk()
    root.title("Genres")
    root.geometry("1250x750")
    # Labels
    welcome = Label(root, text="Check out these Genres!!!",
                    font=('roboto', 50), anchor=CENTER)
    welcome.grid(row=0, column=0, columnspan=3, padx=45,
                 pady=20)
    # Buttons
    actionAdventure = Button(root, text="Action and Adventure",
                command=lambda: view("Action and Adventure"),
                font=('roboto', 36))
    actionAdventure.grid(row=1, column=0, pady=10,
                   ipadx=68, ipady=20)

    anime = Button(root, text="Animation",
                  command=lambda: view("Animation"),
                  font=('roboto', 36))
    anime.grid(row=1, column=1, pady=10,
                   ipadx=68, ipady=20)

    comedy = Button(root, text="Comedy",
                  command=lambda: view("Comedy"),
                  font=('roboto', 36))
    comedy.grid(row=1, column=2, pady=10,
                   ipadx=68, ipady=20)

    crime = Button(root, text="Crime",
                       command=lambda: view("Crime"),
                       font=('roboto', 36))
    crime.grid(row=2, column=0, pady=10,
                   ipadx=68, ipady=20)

    docu = Button(root, text="Documentary",
                   command=lambda: view("Documentary"),
                   font=('roboto', 36))
    docu.grid(row=2, column=1, pady=10,
                   ipadx=68, ipady=20)

    drama = Button(root, text="Drama",
                      command=lambda: view("Drama"),
                      font=('roboto', 36))
    drama.grid(row=2, column=2, pady=10,
                   ipadx=68, ipady=20)
    
    fantasy = Button(root, text="Fantasy",
                   command=lambda: view("Fantasy"),
                   font=('roboto', 36))
    fantasy.grid(row=3, column=0, pady=10,
                   ipadx=68, ipady=20)

    horror = Button(root, text="Horror",
                   command=lambda: view("Horror"),
                   font=('roboto', 36))
    horror.grid(row=3, column=1, pady=10,
                   ipadx=68, ipady=20)

    romance = Button(root, text="Romance",
                   command=lambda: view("Romance"),
                   font=('roboto', 36))
    romance.grid(row=3, column=2, pady=10,
                   ipadx=68, ipady=20)

    scifi = Button(root, text="Science Fiction",
                   command=lambda: view("Science Fiction"),
                   font=('roboto', 36))
    scifi.grid(row=4, column=0, pady=10,
                   ipadx=68, ipady=20)
    
    thriller = Button(root, text="Thriller",
                   command=lambda: view("Thriller"),
                   font=('roboto', 36))
    thriller.grid(row=4, column=1, pady=10,
                   ipadx=68, ipady=20)
    
    western = Button(root, text="Western",
                   command=lambda: view("Western"),
                   font=('roboto', 36))
    western.grid(row=4, column=2, pady=10,
                   ipadx=68, ipady=20)

    terminate = Button(root, text="Close This Window", command=root.destroy,
                       font=('roboto', 36))
    terminate.grid(row=5, column=0, columnspan=3,
                   pady=10, ipadx=90, ipady=20)
    root.mainloop()
