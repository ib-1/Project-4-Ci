from django.urls import path
from .views import rooms, books

app_name = 'Booking'

urlpatterns = [
    path('rooms/', rooms.as_view(), name='rooms'),
    path('books/', books.as_view(), name='books'),
]
