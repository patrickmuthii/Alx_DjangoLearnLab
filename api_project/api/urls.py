from django.urls import path, include
from .views import BookList
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'books', BookList)

urlpatterns = [
    path('books/', BookList.as_view(), name='book_list'),
    path('', include(router.urls))
]