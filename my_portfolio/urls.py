from django.urls import path, re_path
from .views import (
    home, my_projects,
    contacts,
)

urlpatterns = [
    path('', home, name = 'home'),
    path('my_projects/', my_projects, name = 'my_projects'),
    path('contacts/', contacts, name = 'contacts')
]