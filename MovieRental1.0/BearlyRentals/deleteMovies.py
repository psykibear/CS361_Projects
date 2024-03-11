import json
from tkinter import *


def checkDeletion(index):
    term = Tk()
    term.title("Delete?")
    term.geometry("4500x250")

    prompt = Label(term, text="Are you sure to delete it?",
                   font=('roboto', 24), anchor=CENTER)
    prompt.grid(row=0, column=0, columnspan=2, padx=45,
                pady=20)

    yes = Button(term, text="Yes",
                 command=lambda: delete(index),
                 font=('roboto', 18))
    yes.grid(row=1, column=0, pady=10,
             ipadx=25, ipady=10)

    no = Button(term, text="No",
                command=term.destroy,
                font=('roboto', 18))
    no.grid(row=1, column=1, pady=10,
            ipadx=25, ipady=10)
    term.mainloop()


def delete(index):
    with open('stock.json', 'r') as infile:
        movies = json.load(infile)

    if index in movies['member']:
        if movies['member'][index]['status'] == 'DELETED':
            message = "\nThe movie's status is already \ndeleted in the system.\n"
        else:
            movies['member'][index]['status'] = 'DELETED'
            with open('stock.json', 'w') as outfile:
                json.dump(movies, outfile, indent=4)
            message = "\nYou successfully deleted the movie.\nmovie status updated.\n"
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


def deleteMovie():
    root = Tk()
    root.title("Delete a movie")
    root.geometry("650x450")
    welcome = Label(root, text="Delete a movie at Bearly Rentals",
                    font=('roboto', 40), anchor=CENTER)
    welcome.grid(row=0, column=0, columnspan=3, padx=45,
                 pady=20)
    prompt = Label(root, text="Please type in the movie's index: ",
                   font=('roboto', 18), anchor=CENTER)
    prompt.grid(row=1, column=0, padx=40, pady=40)
    index = Entry(root, width=10)
    index.grid(row=1, column=1)

    submitB = Button(root, text="SUBMIT",
                     command=lambda: delete(index.get()),
                     font=('roboto', 18))
    submitB.grid(row=2, column=0, columnspan=2,
                 pady=10, ipadx=20, ipady=10)

    terminate = Button(root, text="Close This Window", command=root.destroy,
                       font=('roboto', 24))
    terminate.grid(row=3, column=0, columnspan=2,
                   pady=10, ipadx=20, ipady=10)
    root.mainloop()
