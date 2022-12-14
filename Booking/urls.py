from django.urls import path
from .views import rooms, books, bookingView

app_name = 'Booking'

urlpatterns = [
    path('rooms/', rooms.as_view(), name='rooms'),
    path('books/', books.as_view(), name='books'),
    path('book/', bookingView.as_view(), name='booking_view'),
]
