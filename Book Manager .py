import json

# Load data from file on startup
try:
    with open("library.txt", "r") as f:
        library = json.load(f)
except FileNotFoundError:
    library = []

# Function to add a book
def add_book():
    title = input("Title: ")
    author = input("Author: ")
    year = input("Year of publication: ")
    library.append({"Title": title, "Author": author, "Year": year})
    print("Book added successfully!")

# Function to search for a book
def search_book():
    title = input("Enter the title of the book to search: ")
    books = [book for book in library if book["Title"].lower() == title.lower()]
    if books:
        for book in books:
            print(f"Title: {book['Title']}, Author: {book['Author']}, Year: {book['Year']}")
    else:
        print("Book not found.")

# Function to display all books
def display_books():
    if not library:
        print("No books in the library.")
    else:
        print("List of books:")
        for book in library:
            print(f"{book['Title']} - {book['Author']} ({book['Year']})")

# Function to delete a book
def delete_book():
    title = input("Enter the title of the book to delete: ")
    global library
    library = [book for book in library if book["Title"].lower() != title.lower()]
    print("Book deleted successfully!")

# Function to save books to file
def save():
    with open("library.txt", "w") as f:
        json.dump(library, f)
    print("Data saved.")

# Menu for the user
while True:
    print("\nMenu:")
    print("1. Add a book")
    print("2. Search for a book")
    print("3. Display all books")
    print("4. Delete a book")
    print("5. Quit and save")
    
    choice = input("Choose an option: ")
    
    if choice == "1":
        add_book()
    elif choice == "2":
        search_book()
    elif choice == "3":
        display_books()
    elif choice == "4":
        delete_book()
    elif choice == "5":
        save()
        break
    else:
        print("Invalid option, please try again.")
