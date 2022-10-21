books = input().split("&")

data = input()

while not data == "Done":
    command = data.split(" | ")
    if command[0] == "Add Book":
        book = command[1]
        if book not in books:
            books.insert(0, book)
    elif command[0] == "Take Book":
        book = command[1]
        if book in books:
            books.remove(book)
    elif command[0] == "Swap Books":
        first = command[1]
        second = command[2]
        if first in books and second in books:
            first_book_ind = books.index(first)
            second_book_ind = books.index(second)
            books[first_book_ind], books[second_book_ind] = books[second_book_ind], books[first_book_ind]
    elif command[0] == "Insert Book":
        book = command[1]
        books.append(book)
    elif command[0] == "Check Book":
        ind = int(command[1])
        if ind < len(books):
            print(books[ind])
    data = input()

print(f"{', '.join(books)}")