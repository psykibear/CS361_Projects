from tkinter import Tk, simpledialog, messagebox
from Movie import MovieLibrary
import UI


def display_home_page():
    # Adjusted to be a method, allowing access to class attributes and methods
    UI.clear()  # Assuming this clears the console
    UI.homePage()  # Display home page options
    choice = simpledialog.askstring("Input",
                                    "Please choose one of the options above by "
                                    "typing in the corresponding number (1-6):")
    return choice


def ask_repeat(function, message):
    answer = messagebox.askyesno("Question", message)
    if answer:
        function()
    else:
        display_home_page()


class LibraryApp:
    def __init__(self):
        self.root = Tk()
        self.root.title("Bearly Rentals")
        self.movie_library = MovieLibrary()  # Create an instance of MovieLibrary
        self.run_app()

    def handle_choice(self, choice):
        if choice == '1':
            self.view_library()
        elif choice == '2':
            self.add_movie()
        elif choice == '3':
            self.rent_movie()
        elif choice == '4':
            self.return_movie()
        elif choice == '5':
            self.delete_movie()
        elif choice == '6':
            self.exit_app()
        else:
            messagebox.showerror("Error",
                                 "\nInvalid Option"
                                 "\nPlease choose one of the options above by typing in the corresponding number:")

    def view_library(self):
        UI.clear()
        UI.category()
        self.movie_library.list_by_category()  # Correctly use the instance
        ask_repeat(self.view_library, "Enter Y to view another category."
                                      "\nEnter N to Home Page.\n")

    def add_movie(self):
        UI.clear()
        self.movie_library.add_movie()
        ask_repeat(self.add_movie, "\nDo you want to add another movie?"
                                   "\nEnter Y to add another movie."
                                   "\nEnter N to Home Page.\n")

    def rent_movie(self):
        UI.clear()
        self.movie_library.perform_action('rent')
        ask_repeat(self.rent_movie, "\nDo you want to rent another movie?"
                                    "\nEnter Y to rent another movie."
                                    "\nEnter N to Home Page.\n")

    def return_movie(self):
        UI.clear()
        self.movie_library.perform_action('return')
        ask_repeat(self.return_movie, "\nDo you want to return another movie?"
                                      "\nEnter Y to return another movie."
                                      "\nEnter N to Home Page.\n")

    def delete_movie(self):
        UI.clear()
        self.movie_library.perform_action('delete')
        ask_repeat(self.delete_movie, "\nDo you want to delete another movie?"
                                      "\nEnter Y to delete another movie."
                                      "\nEnter N to Home Page.\n")

    def exit_app(self):
        exitAnswer = messagebox.askyesno("Exit", "Are you sure you want to exit?")
        if exitAnswer:
            print("\nThanks for visiting Bearly Rentals, goodbye!\n")
            self.root.quit()  # Use quit to end the Tkinter mainloop
            self.root.destroy()  # Ensure all windows are closed

    def run_app(self):
        self.root.withdraw()  # Hide the main window as we're using dialogues
        while True:
            choice = display_home_page()
            self.handle_choice(choice)


if __name__ == '__main__':
    LibraryApp()
