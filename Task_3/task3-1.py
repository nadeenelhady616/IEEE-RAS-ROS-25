library = {
    "1": {
        "title": "Harry potter",
        "author": "J.K Rowling",
        "publication_year": 1998
    },
    "2": {
        "title": "Pride and Prejudice",
        "author": "Jane Austen",
        "publication_year": 1813
    },
    "3": {
        "title": "Babel",
        "author": "R.F kuang",
        "publication_year": 2022
    }
}
key = input("enter index to get its book:")
print(library.get(key))
