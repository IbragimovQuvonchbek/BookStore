import requests

# Example URL for your Django server running locally
base_url = 'http://127.0.0.1:8000/api/v1/'

# Example data for creating a new book
# new_book_data = {
#     'title': 'New Book Title',
#     'description': 'New Book Description',
#     'author': 'New Book Author',
#     'year': '2022',
#     'pages': '200',
#     'username': 'newuser'
# }

# Example API link to create a new book
# create_book_url = base_url + 'create-book/'
# response = requests.post(create_book_url, json=new_book_data)
# print('Create Book API Response:', response.status_code)

# Example API link to get a list of books
book_list_url = base_url + 'book-list/'
response = requests.get(book_list_url)
# print('Book List API Response:', response.status_code)
print('Book List:', response.json())

# Example API link to get details of a specific book (assuming book_id is 1)
# book_detail_url = base_url + 'book-detail/5/'
# response = requests.get(book_detail_url)
# print('Book Detail API Response:', response.status_code)
# print('Book Detail:', response.json())

# Example data for deleting a book (assuming book_id is 1)
# delete_book_data = {
#     'id': 4,
#     'username': 'newuser'
# }

# # Example API link to delete a book
# delete_book_url = base_url + 'book-delete/'
# response = requests.delete(delete_book_url, json=delete_book_data)
# print('Delete Book API Response:', response.status_code)

# Example data for updating a book (assuming book_id is 1)
update_book_data = {
    'id': 5,
    'title': 'Updated Book Title',
    'description': 'Updated Book Description',
    'author': 'Updated Book Author',
    'year': '2023',
    'pages': '250000',
    'username': 'newuser'
}

# Example API link to update a book
update_book_url = base_url + 'book-update/'
response = requests.put(update_book_url, json=update_book_data)
print('Update Book API Response:', response.status_code)
