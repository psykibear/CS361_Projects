import json
from tkinter import *


def rent(index):
    with open('stock.json', 'r') as infile:
        movies = json.load(infile)

    if index in movies['member']:
        if movies['member'][index]['status'] == 'movie rented':
            message = "\nI am sorry.\nThe movie is currently rented \nby another user.\n"
        elif movies['member'][index]['status'] == 'DELETED':
            message = "\nI am sorry.\nThe movie is no longer available.\n"
        else:
            movies['member'][index]['status'] = 'movie rented'
            with open('stock.json', 'w') as outfile:
                json.dump(movies, outfile, indent=4)
            message = "\nmovie successfully rented!\nmovie status updated.\n"
    else:
        message = "\nINVALID INPUT\nThe index number does not exist.\n"

    update = Tk()
    update.title("System Message")
    update.geometry("240x160")

    mess = Label(update, text=message, font=('roboto', 15))
    mess.grid(row=0, column=0, padx=20)
    close = Button(update, text="Close this window",
                   command=update.destroy,
                   font=('roboto', 18))
    close.grid(row=1, column=0, padx=20, pady=10,
               ipadx=25, ipady=10)
    update.mainloop()


def rentMovie():
    root = Tk()
    root.title("Rent a movie")
    welcome = Label(root, text="Rent a movie from Bearly Rentals",
                    font=('roboto', 40), anchor=CENTER)
    welcome.grid(row=0, column=0, columnspan=3, padx=45,
                 pady=20)
    root.geometry("650x450")
    prompt = Label(root, text="Please type in the movie's index: ",
                   font=('roboto', 18), anchor=CENTER)
    prompt.grid(row=1, column=0, padx=40, pady=40)
    index = Entry(root, width=10)
    index.grid(row=1, column=1)

    submitB = Button(root, text="SUBMIT",
                     command=lambda: rent(index.get()),
                     font=('roboto', 18))
    submitB.grid(row=2, column=0, columnspan=2,
                 pady=10, ipadx=20, ipady=10)

    terminate = Button(root, text="Close This Window", command=root.destroy,
                       font=('roboto', 24))
    terminate.grid(row=3, column=0, columnspan=2,
                   pady=10, ipadx=20, ipady=10)
    root.mainloop()
