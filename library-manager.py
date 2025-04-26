import json

library = []

def load_library():
    try:
        with open("library.txt", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_library():
    with open("library.txt", "w") as file:
        json.dump(library, file)

def add_book():
    title = input("Enter the book title: ")
    author = input("Enter the author: ")
    year = int(input("Enter the publication year: "))
    genre = input("Enter the genre: ")
    read_input = input("Have you read this book? (yes/no): ").strip().lower()
    read = read_input == "yes"
    library.append({
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read": read
    })
    print("Book added successfully!")

def remove_book():
    title = input("Enter the title of the book to remove: ")
    for book in library:
        if book["title"].lower() == title.lower():
            library.remove(book)
            print("Book removed successfully!")
            return
    print("Book not found.")

def search_book():
    choice = input("Search by:\n1. Title\n2. Author\nEnter your choice: ")
    keyword = input("Enter the search keyword: ").lower()
    matches = []
    for book in library:
        if (choice == "1" and keyword in book["title"].lower()) or (choice == "2" and keyword in book["author"].lower()):
            matches.append(book)
    if matches:
        print("Matching Books:")
        for idx, book in enumerate(matches, 1):
            read_status = "Read" if book["read"] else "Unread"
            print(f"{idx}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {read_status}")
    else:
        print("No matching books found.")

def display_books():
    if not library:
        print("Library is empty.")
        return
    print("Your Library:")
    for idx, book in enumerate(library, 1):
        read_status = "Read" if book["read"] else "Unread"
        print(f"{idx}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {read_status}")

def display_statistics():
    total = len(library)
    if total == 0:
        print("No books in the library.")
        return
    read_books = sum(book["read"] for book in library)
    percentage_read = (read_books / total) * 100
    print(f"Total books: {total}")
    print(f"Percentage read: {percentage_read:.1f}%")

def main():
    global library
    library = load_library()
    while True:
        print("\nMenu\nWelcome to your Personal Library Manager!")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. Display all books")
        print("5. Display statistics")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            remove_book()
        elif choice == "3":
            search_book()
        elif choice == "4":
            display_books()
        elif choice == "5":
            display_statistics()
        elif choice == "6":
            save_library()
            print("Library saved to file. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
