import json
from tkinter import *


def returnRented(index, loc):
    with open('stock.json', 'r') as infile:
        movies = json.load(infile)
    if index in movies['member']:
        if movies['member'][index]['status'] == 'movie rented':
            movies['member'][index]['location'] = loc
            movies['member'][index]['status'] = "On Shelf at " + movies['member'][index]['location']
            with open('stock.json', 'w') as outfile:
                json.dump(movies, outfile, indent=4)
            message = "\nmovie returned successfully!\nmovie status updated.\n"
        else:
            message = "\nSystem info mismatched.\nPlease contact CLowe.\n"
    else:
        message = "\nINVALID INPUT\nThe index does not exist."

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


def returnMovie():
    root = Tk()
    root.title("Return a movie")
    root.geometry("650x450")
    welcome = Label(root, text="Return a movie to Bearly Rentals",
                    font=('roboto', 40), anchor=CENTER)
    welcome.grid(row=0, column=0, columnspan=3, padx=45,
                 pady=20)
    prompt = Label(root, text="Please type in the movie's index: ",
                   font=('roboto', 18), anchor=CENTER)
    prompt.grid(row=1, column=0, padx=40, pady=20)
    locationLabel = Label(root, text="Where do you put it?",
                          font=('roboto', 18), anchor=CENTER)
    locationLabel.grid(row=2, column=0, padx=40, pady=20)
    index = Entry(root, width=10)
    index.grid(row=1, column=1)
    loc = Entry(root, width=10)
    loc.grid(row=2, column=1)

    submitB = Button(root, text="SUBMIT",
                     command=lambda: returnRented(index.get(), loc.get()),
                     font=('roboto', 18))
    submitB.grid(row=3, column=0, columnspan=2, 
                 pady=10, ipadx=20, ipady=10)

    terminate = Button(root, text="Close This Window", command=root.destroy,
                       font=('roboto', 24))
    terminate.grid(row=4, column=0, columnspan=2,
                   pady=10, ipadx=20, ipady=10)
    root.mainloop()
