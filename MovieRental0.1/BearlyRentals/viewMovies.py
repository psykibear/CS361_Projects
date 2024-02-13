import json
from tkinter import *


def view(cat):
    output = "For " + cat + " category, we have:\n"
    with open('stock.json', 'r') as infile:
        movies = json.load(infile)
    for movie in movies['member']:
        if movies['member'][movie]['category'] == cat:
            output += ('\t' + movie + '. ' + movies['member'][movie]['name'] + '\n\t----' +
                       movies['member'][movie]['status'] + '\n')
    root = Tk()
    root.title(cat)
    root.geometry("960x1200")
    welcome = Label(root, text="Welcome to Bearly Rentals", font=('roboto', 80), anchor=CENTER)
    welcome.grid(row=0, column=0, columnspan=2, padx=45, pady=20)

    content = Label(root, text=output, font=('roboto', 18), anchor='w', justify=LEFT)
    content.grid(row=1, column=0, columnspan=2, pady=10, ipadx=25, ipady=20)

    terminate = Button(root, text="Close This Window", command=root.destroy, font=('roboto', 24))
    terminate.grid(row=4, column=0, columnspan=2, pady=10, ipadx=90, ipady=20)

    root.mainloop()


def listByCategory():
    root = Tk()
    root.title("Categories")
    root.geometry("960x600")
    # Labels
    welcome = Label(root, text="Welcome to Bearly Rentals", font=('roboto', 80), anchor=CENTER)
    welcome.grid(row=0, column=0, columnspan=2, padx=45, pady=20)
    # Buttons
    AA = Button(root, text="Action and Adventure", command=lambda: view("Action and Adventure"), font=('roboto', 36))
    AA.grid(row=1, column=0, pady=10, ipadx=10, ipady=20)

    anime = Button(root, text="Animation", command=lambda: view("Animation"), font=('roboto', 36))
    anime.grid(row=1, column=1, pady=10, ipadx=45, ipady=20)

    comedy = Button(root, text="Comedy", command=lambda: view("Comedy"), font=('roboto', 36))
    comedy.grid(row=2, column=0, pady=10, ipadx=62, ipady=20)

    crime = Button(root, text="Crime", command=lambda: view("Crime"), font=('roboto', 36))
    crime.grid(row=2, column=1, pady=10, ipadx=68, ipady=20)

    drama = Button(root, text="Drama", command=lambda: view("Drama"), font=('roboto', 36))
    drama.grid(row=3, column=0, pady=10, ipadx=83, ipady=20)

    horror = Button(root, text="Horror", command=lambda: view("Horror"), font=('roboto', 36))
    horror.grid(row=3, column=1, pady=10, ipadx=83, ipady=20)

    scififan = Button(root, text="SciFi and Fantasy", command=lambda: view("SciFi and Fantasy"), font=('roboto', 36))
    scififan.grid(row=4, column=0, pady=10, ipadx=88, ipady=20)

    thriller = Button(root, text="Thriller", command=lambda: view("Thriller"), font=('roboto', 36))
    thriller.grid(row=4, column=1, pady=10, ipadx=88, ipady=20)

    terminate = Button(root, text="Close This Window", command=root.destroy, font=('roboto', 36))
    terminate.grid(row=5, column=0, columnspan=2, pady=10, ipadx=90, ipady=20)
    root.mainloop()
