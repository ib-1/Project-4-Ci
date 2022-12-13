import datetime
from Booking.models import room, book

def check_availibility(room, checking_in, checking_out):
    availibility_list=[]
    book_list = book.objects.filter(room=room)
    for books in book_list:
        if books.checking_in > checking_out or books.checking_out < checking_in:
            availibility_list.append(True)
        else:
            availibility_list.append(False)
    return all(availibility_list)

