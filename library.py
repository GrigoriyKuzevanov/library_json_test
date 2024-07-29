import argparse
import json
from argparse import Namespace

# функции для выполнения операциий с базой данных (файл .json)
def create_json(args: Namespace, file_name: str = "db.json"):
    """
    Create a .json file in project directory
    with file_name parameter's name
    and starting books structure.
    Print message to console if succeed.
    """
    with open(file_name, "w+", encoding="utf-8") as f:
        db: dict = {"books": []}
        json.dump(db, f, indent=4, ensure_ascii=False)
        print("json file is created")


def list_books(args: Namespace):
    """
    Print to console list of books from
    db .json file or message if file is empty
    """
    with open("db.json", encoding="utf-8") as f:
        db: dict = json.load(f)
        if db["books"]:
            for book in db["books"]:
                print(book)
        else:
            print("db is empty")


def add_book(args: Namespace, file_name: str = "db.json"):
    """
    Rewrite db .json file with added book using given
    parametres, create unique id for added book.
    Print message to console if succeed.
    """
    with open(file_name, "r", encoding="utf-8") as f:
        db: dict = json.load(f)

    max_book_id = 0
    for book in db["books"]:
        if book["id"] > max_book_id:
            max_book_id = book["id"]

    data = {
        "id": max_book_id + 1,
        "title": args.book_title,
        "author": args.book_author,
        "year": args.book_year,
        "status": args.book_status,
    }

    db["books"].append(data)

    with open(file_name, "w", encoding="utf-8") as f:
        json.dump(db, f, indent=4, ensure_ascii=False)
        print("book is added")


def delete_book(args: Namespace, file_name: str = "db.json"):
    """
    Rewrite db .json file with deleting book by given id.
    Print message to console if succeed or if book with
    given id is not found.
    """
    with open(file_name, "r", encoding="utf-8") as f:
        db: dict = json.load(f)

    book_id: int = args.book_id

    for book in db["books"]:
        if book["id"] == book_id:
            db["books"].remove(book)
            break
    else:
        print(f"book with id: {book_id} is not found")
        return None

    with open(file_name, "w", encoding="utf-8") as f:
        json.dump(db, f, indent=4, ensure_ascii=False)
        print(f"book with id: {book_id} is deleted")


def change_status(args: Namespace, file_name: str = "db.json"):
    """
    Rewrite db .json file with changing book.status field
    with given id. Print message to console if succeed or
    if book with given id is not found.
    """
    with open(file_name, "r", encoding="utf-8") as f:
        db: dict = json.load(f)

    book_id: int = args.book_id
    new_status: str = args.new_status

    for book in db["books"]:
        if book["id"] == book_id:
            book["status"] = new_status
            print(book)
            break
    else:
        print(f"book with id: {book_id} is not found")
        return None

    with open(file_name, "w", encoding="utf-8") as f:
        json.dump(db, f, indent=4, ensure_ascii=False)
        print("status was changed")
        


def search_book(args: Namespace):
    """
    Open db .json file and search on fields
    book.title, book.author, book.year with
    given parameter. Print results to console.
    """
    with open("db.json", "r", encoding="utf-8") as f:
        db: dict = json.load(f)

    search_query: str = args.search_query

    for book in db["books"]:
        if search_query in (book["title"], book["author"], book["year"]):
            print(book)


# create parser of command line arguments
parser = argparse.ArgumentParser(prog="library.py")

subparsers = parser.add_subparsers(
    title="Library operating", description="Available commands", help="description"
)


# parser for create json file in project directory 
create_json_parser = subparsers.add_parser("create-json", help="create db.json")
create_json_parser.set_defaults(func=create_json)


# parser for add book args
add_parser = subparsers.add_parser("add", help="add new book")
add_parser.add_argument("book_title", help="book's title", metavar="TITLE", type=str)
add_parser.add_argument("book_author", help="book's author", metavar="AUTHOR", type=str)
add_parser.add_argument("book_year", help="book's year", metavar="YEAR", type=str)
add_parser.add_argument(
    "book_status",
    help="book's status",
    metavar="STATUS",
    choices=["в наличии", "выдана"],
)
add_parser.set_defaults(func=add_book)


# parser for delete book args
delete_parser = subparsers.add_parser("delete", help="delete book by id")
delete_parser.add_argument("book_id", help="delete book by id", metavar="ID", type=int)
delete_parser.set_defaults(func=delete_book)


# parser for search books args
search_parser = subparsers.add_parser(
    "search", help="search book by title, author or year"
)
search_parser.add_argument(
    "search_query", help="search query", metavar="QUERY", type=str
)
search_parser.set_defaults(func=search_book)


# parser for list books args
list_parser = subparsers.add_parser("list", help="list all books")
list_parser.set_defaults(func=list_books)


# parser for changing book's status args
change_status_parser = subparsers.add_parser("change", help="change book's status")
change_status_parser.add_argument("book_id", help="new status", metavar="ID", type=int)
change_status_parser.add_argument(
    "new_status", help="new status", metavar="ST", choices=["выдана", "в наличии"]
)
change_status_parser.set_defaults(func=change_status)


if __name__ == "__main__":
    args = parser.parse_args()
    if not vars(args):
        parser.print_usage()
    else:
        try:
            args.func(args)
        except FileNotFoundError as e:
            print(f"Error message: {e}")
            print("You should create json file first with create command")
