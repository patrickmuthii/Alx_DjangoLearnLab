from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from api.models import Book
from django.contrib.auth.models import User

class BookAPITestCase(APITestCase):

    def setUp(self):
        # Set up initial data for testing
        self.user = User.objects.create_user(username='patrick', password='patorocky')
        self.book1 = Book.objects.create(title='psychology of money', author='Morgan Housel', publication_year=2021)
        self.book2 = Book.objects.create(title='Trading bulls', author='Twain', publication_year=2022)
        self.client.login(username='patrick', password='patorocky')
# test on how to create a book using the post method
    def test_create_book(self):
        url = reverse('book-list')
        data = {'title': 'New Book', 'author': 'New Author', 'publication_year': 2023}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)
# test on how to get a book using the get method
    def test_retrieve_book(self):
        url = reverse('book-detail', args=[self.book1.id])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book1.title)

# test on how to update a book using the put method
    def test_update_book(self):
        url = reverse('book-detail', args=[self.book1.id])
        data = {'title': 'Updated Title', 'author': self.book1.author, 'publication_year': self.book1.publication_year}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, 'Updated Title')

# test on how to delete a book using the delete method
    def test_delete_book(self):
        url = reverse('book-detail', args=[self.book1.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

# test on how to filter books using the get method
    def test_filter_books(self):
        url = f"{reverse('book-list')}?author=Morgan Housel"
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['author'], 'Morgan Housel')

# test on how to search books using the get method
    def test_search_books(self):
        url = f"{reverse('book-list')}?search=psychology of money"
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'psychology of money')

# test on how to order books using the get method
    def test_order_books(self):
        url = f"{reverse('book-list')}?ordering=publication_year"
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], 'psychology of money')  # Assuming ascending order by default

# test on how to restrict access to books using the post method
    def test_permissions(self):
        self.client.logout()  
        url = reverse('book-list')
        response = self.client.post(url, {'title': 'Unauthorized Book'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
