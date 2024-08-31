from django.urls import path
from .views import BookList
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'books', BookList)

urlpatterns = [
    path('books/', BookList.as_view(), name='book_list'),
    *router.urls
]