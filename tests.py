import json
import pathlib
import unittest
from argparse import Namespace

from library import add_book, change_status, delete_book

TEST_FILE_NAME = "db-test.json"
DATA_FOR_SET_UP = {
    "books": [
        {
            "id": 100,
            "title": "set_title",
            "author": "set_author",
            "year": "set_year",
            "status": "выдана",
        },
        {
            "id": 200,
            "title": "set_title-2",
            "author": "set_author-2",
            "year": "set_year-2",
            "status": "выдана",
        },
    ]
}


class TestJsonLibrary(unittest.TestCase):
    def setUp(self):
        with open(TEST_FILE_NAME, "w+", encoding="utf-8") as f:
            json.dump(DATA_FOR_SET_UP, f, indent=4, ensure_ascii=False)

    def tearDown(self):
        file_to_remove = pathlib.Path(TEST_FILE_NAME)
        if file_to_remove.is_file():
            file_to_remove.unlink()

    def test_add_book(self):
        """
        Test library.add_book function by adding new book with specified args
        and reading test .json file. Check equality of given args and 
        reading book fields. Also check len of books list before and after adding book.
        """
        args = Namespace(
            book_title="test title",
            book_author="test author",
            book_year="test year",
            book_status="выдана",
        )

        with open(TEST_FILE_NAME, encoding="utf-8") as f:
            db_before: dict = json.load(f)
            current_length: int = len(db_before["books"])

        add_book(args, file_name=TEST_FILE_NAME)

        with open(TEST_FILE_NAME, encoding="utf-8") as f:
            db_after: dict = json.load(f)

        self.assertEqual(len(db_after["books"]), current_length + 1)
        self.assertEqual(db_after["books"][-1]["title"], args.book_title)
        self.assertEqual(db_after["books"][-1]["author"], args.book_author)
        self.assertEqual(db_after["books"][-1]["year"], args.book_year)
        self.assertEqual(db_after["books"][-1]["status"], args.book_status)

    def test_change_status(self):
        """
        Test library.change_status function by changing status
        of two preset books, reading test .json file and checking
        equality of given statuses and reading statuses.
        """
        args = Namespace(book_id=100, new_status="в наличии")
        args_vars = (
            Namespace(book_id=100, new_status="в наличии"),
            Namespace(book_id=200, new_status="в наличии"),
        )
        for args in args_vars:
            change_status(args, file_name=TEST_FILE_NAME)

        with open(TEST_FILE_NAME, encoding="utf-8") as f:
            db: dict = json.load(f)

        for book in db["books"]:
            self.assertEqual(book["status"], "в наличии")

    def test_delete_book(self):
        """
        Test library.delete_book function by deleting book by specified id.
        Check len of books list before and after deleting book.
        """
        args = Namespace(book_id=100)
        with open(TEST_FILE_NAME, encoding="utf-8") as f:
            db_before: dict = json.load(f)
            current_length: int = len(db_before["books"])

        delete_book(args, file_name=TEST_FILE_NAME)

        with open(TEST_FILE_NAME, encoding="utf-8") as f:
            db_after = json.load(f)

        self.assertEqual(len(db_after["books"]), current_length - 1)


if __name__ == "__main__":
    unittest.main()
