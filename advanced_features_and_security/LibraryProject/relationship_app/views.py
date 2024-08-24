
# from .models import Book, Author, Librarian
# from django.views.generic.detail import DetailView
# from django.http import HttpResponse
# from .models import Library
# from django.shortcuts import render, redirect
# from django.contrib.auth import login as auth_login, logout as auth_logout
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from django.contrib.auth.decorators import login_required
# from typing import Any
# from django.shortcuts import render,redirect
# from .models import Book, Library
# from django.views.generic.detail import DetailView
# from django.contrib.auth.decorators import login_required, user_passes_test
# from django.contrib.auth.views import LoginView, LogoutView
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth import login
# from django.contrib.auth.decorators import permission_required

# def list_books(request):
#     books = Book.objects.all()
#     return render(request, 'relationship_app/list_books.html', {'books': books})


# class LibraryDetailView(DetailView):
#     model = Library
#     template_name = 'relationship_app/library_detail.html'
#     context_object_name = 'library'





# def login_view(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             auth_login(request, user)
#             return redirect('home')  # Redirect to a home page or dashboard
#     else:
#         form = AuthenticationForm()
#     return render(request, 'relationship_app/login.html', {'form': form})

# def logout_view(request):
#     if request.method == 'POST':
#         auth_logout(request)
#         return redirect('logout_done')
#     return render(request, 'relationship_app/logout.html')

# def register_view(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('login')
#     else:
#         form = UserCreationForm()
#     return render(request, 'relationship_app/register.html', {'form': form})

# #Setting Up Role-Based Views
# #Checks if user is Admin

#  def index(request):
#      return render(request, "index.html")

# def is_admin(user):
#     return user.userprofile.role == 'Admin'


# @login_required
# @user_passes_test(is_admin)
# def admin_view(request):
#     return render(request, 'relationship_app/admin_view.html')

# #Checks if user is Librarian
# def is_librarian(user):
#     return user.userprofile.role == 'Librarian'

# @login_required
# @user_passes_test(is_librarian)

# def librarian_view(request):
#     return render(request, 'relationship_app/librarian_view.html')

# #Checks if user is a Member
# def is_member(user):
#     return user.userprofile.role == 'Member'

# @login_required
# @user_passes_test(is_member)
# def member_view(request):
#     return render(request, 'relationship_app/member_view.html')

#Views to Enforce Permissions
# @permission_required("relationship_app.can_add_book")
# def can_add_book_view(request):
#     return render(request, 'relationship_app/can_add_book.html')

# @permission_required("relationship_app.can_change_book")
# def can_change_book_view(request):
#     return render(request, 'relationship_app/can_change_book.html')

# @permission_required("relationship_app.can_delete_book")
# def can_delete_book_view(request):
#     return render(request, 'relationship_app/can_delete_book')


from typing import Any
from django.shortcuts import render,redirect
from .models import Book, Library
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required, user_passes_test, permission_required
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import permission_required



# Create your views here.
#Function-based views
def list_books(request):
    books = Book.objects.all() #fetching all books from the database
    context = {'list_books':books} #creates a context dictionary with list of books
    return render(request, 'relationship_app/list_books.html', context)

#class-based view for listing books in a library
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        library = self.get_object()
        context['books_list'] = library.get_books_list()
        return context
    

#Setup User Authentication Views

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect ("index")
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})

#User Login View
class CustomLoginView(LoginView):
    template_name = "login.html"

#user Logout View
class CustomLogoutView(LogoutView):
    template_name = "logout.html"

#Homepage View
def index(request):
    return render(request, "index.html")

#Setting Up Role-Based Views
#Checks if user is Admin
def is_admin(user):
    return user.userprofile.role == 'Admin'

@login_required
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

#Checks if user is Librarian
def is_librarian(user):
    return user.userprofile.role == 'Librarian'

@login_required
@user_passes_test(is_librarian)

def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

#Checks if user is a Member
def is_member(user):
    return user.userprofile.role == 'Member'

@login_required
@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')

#Views to Enforce Permissions
@permission_required("relationship_app.can_add_book")
def can_add_book_view(request):
    return render(request, 'relationship_app/can_add_book.html')

@permission_required("relationship_app.can_change_book")
def can_change_book_view(request):
    return render(request, 'relationship_app/can_change_book.html')

@permission_required("relationship_app.can_delete_book")
def can_delete_book_view(request):
    return render(request, 'relationship_app/can_delete_book.html')
