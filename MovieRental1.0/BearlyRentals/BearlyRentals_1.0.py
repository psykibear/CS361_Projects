from tkinter import *
from viewMovies import listByGenre
from addMovies import addMovie
from deleteMovies import deleteMovie
from rentMovies import rentMovie
from returnMovies import returnMovie
from randomRecommendation import randomRec


def checkExit():
    term = Tk()
    term.title("Exit?")
    term.geometry("300x160")

    prompt = Label(term, text="Do you want to exit?",
                   font=('roboto', 24), anchor=CENTER)
    prompt.grid(row=0, column=0, columnspan=2, padx=45,
                pady=20)

    yes = Button(term, text="Yes",
                 command=exit,
                 font=('roboto', 18))
    yes.grid(row=1, column=0, pady=10,
             ipadx=25, ipady=10)

    no = Button(term, text="No",
                command=term.destroy,
                font=('roboto', 18))
    no.grid(row=1, column=1, pady=10,
            ipadx=25, ipady=10)
    term.mainloop()


if __name__ == '__main__':
    root = Tk()
    root.title("Bearly Rentals!!!")
    root.geometry("1100x750")

    # Labels
    welcome = Label(root, text="Welcome to Bearly Rentals!!!",
                    font=('roboto', 80), anchor=CENTER)
    welcome.grid(row=0, column=0, columnspan=2, padx=45,
                 pady=20)

    # Buttons
    view = Button(root, text="Browse by Genre", command=listByGenre,
                  font=('roboto', 42))
    view.grid(row=1, column=0, columnspan=2, pady=10,
              ipadx=142, ipady=20)
    
    rent = Button(root, text="Rent a Movie", command=rentMovie,
                    font=('roboto', 42))
    rent.grid(row=2, column=0, pady=10,
                ipadx=21, ipady=20)

    returnM = Button(root, text="Return a Movie", command=returnMovie,
                     font=('roboto', 42))
    returnM.grid(row=2, column=1, pady=10,
                 ipadx=43, ipady=20)

    add = Button(root, text="Add a Movie", command=addMovie,
                 font=('roboto', 42))
    add.grid(row=3, column=0, pady=10,
             ipadx=45, ipady=20)

    delete = Button(root, text="Delete a Movie", command=deleteMovie,
                    font=('roboto', 42))
    delete.grid(row=3, column=1, pady=10,
                ipadx=45, ipady=20)

    RR = Button(root, text="Random Movie Game!!!",
                command=randomRec,
                font=('roboto', 42))
    RR.grid(row=4, column=0, pady=10, columnspan=3,
            ipadx=142, ipady=20)

    terminate = Button(root, text="Exit", command=checkExit,
                       font=('roboto', 42))
    terminate.grid(row=5, column=0, columnspan=3,
                   pady=10, ipadx=142, ipady=20)

    root.mainloop()
