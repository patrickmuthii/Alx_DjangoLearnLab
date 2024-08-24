from django.urls import path
from . import views
from .views import admin_view
from django.contrib.auth.views import LoginView, LogoutView
from .views import list_books, LibraryDetailView, register_view, index
urlpatterns = [
    path('', index, name='index'),
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('logout/done/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout_done'),
    path('register/', views.register, name='register'),
    path('admin_view/', views.admin_view, name='admin_view'),
    path('librarian_view/', views.librarian_view, name='librarian_view'),
    path('member_view/', views.member_view, name='member_view'),
    path("add_book/", views.can_add_book_view, name='can_add_book_view'),
    path("edit_book/", views.can_change_book_view, name='can_change_book_view'),
    path("can_delete_book_view/", views.can_delete_book_view, name='can_delete_book_view'),

]