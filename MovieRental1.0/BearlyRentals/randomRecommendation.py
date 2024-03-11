import json
import requests
from tkinter import *

def fetch_random_number(max_val):
    url = f"http://localhost:3050/api/random?max={max_val}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data.get("number")
    else:
        return -1  # Indicate an error if the service call failed

def randomRec():
    with open('stock.json', 'r') as infile:
        movies = json.load(infile)
    inventory = len(movies['member']) 

    index = fetch_random_number(inventory)
    # Convert index to a string if your keys are strings or adjust accordingly
    index_key = str(index)

    RR = Tk()
    RR.title("Random Movie Game!!")
    RR.geometry("750x450")

    welcome = Label(RR, text="Random Movie Game", font=('roboto', 30), anchor=CENTER)
    welcome.grid(row=0, column=0, columnspan=3, padx=45, pady=20)

    if index_key in movies['member']:
        movie = movies['member'][index_key]
        name = movie['name']
        location = movie['location']
        status = movie['status']
        genre = movie['genre']

        info = f'{index}\n{name}\n{location}\n{status}\n{genre}'
    else:
        info = 'Error: RNG Microservice is not initiated or failed to fetch data'

    dataLabel = Label(RR, text=info, font=('roboto', 24), anchor='w', justify=LEFT)
    dataLabel.grid(row=2, column=0, pady=10, ipadx=25, ipady=20)

    terminate = Button(RR, text="Close This Window", command=RR.destroy, font=('roboto', 36))
    terminate.grid(row=5, column=0, columnspan=3, pady=10, ipadx=90, ipady=20)

    RR.mainloop()

if __name__ == "__main__":
    randomRec()
