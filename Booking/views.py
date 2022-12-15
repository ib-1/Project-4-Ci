from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, FormView, View, DeleteView
from django.urls import reverse, reverse_lazy
from .models import room, book
from .forms import availibleFrom
from Booking.book_functions.availibility import check_availibility
# Create your views here.

def rooms(request):
    rooms = room.objects.all()[0]
    room_categories = dict(room.room_type)
    room_values = room_categories.values()
    room_list=[]

    for room_type in room_categories: # loops through the list to create a list of room types to iterate through for the html
        rooms = room_categories.get(room_type)
        room_url = reverse('Booking:roomdetailview', kwargs={'category': room_type})
        room_list.append((rooms, room_url))
    context = {
        "room_list": room_list,
        
    }
    print(room_list)
    return render(request, 'roominfoview.html', context)

class books(ListView):
    model = book
    def get_queryset(self, *args, **kwargs):
        if self.request.user.is_staff:
            booking_list = book.objects.all()
            return booking_list
        else:
            booking_list = book.objects.filter(user=self.request.user)
            return booking_list


class roomdetailview(View):
    def get(self, request, *args, **kwargs):
        category = self.kwargs.get('category', None)
        form = availibleFrom()
        room_list = room.objects.filter(category=category)
        rooms = room_list[0]

        if len(room_list) > 0:
            rooms = room_list[0]
            room_category = dict(room.room_type).get(rooms.category, None)  #creates a dictonaty of the room catergories/types
            context = {
                "room_category": room_category,
                "form": form,
            }
            return render(request, 'roomdetailview.html', context)
        else: 
            return HttpResponse("this room does not exist!")


    def post(self, request, *args, **kwargs):
        category = self.kwargs.get('category', None)
        room_list = room.objects.filter(category=category)
        form = availibleFrom(request.POST)

        if form.is_valid():
            data = form.cleaned_data

        available_room_list = []
        for rooms in room_list:
            if check_availibility(rooms, data['checking_in'], data['checking_out']):
                available_room_list.append(rooms)

        if len(available_room_list) > 0:
            availroom = available_room_list[0]
            availbook = book.objects.create(
                user = self.request.user,
                room = availroom,
                checking_in = data['checking_in'],
                checking_out = data['checking_out'],
            )
            availbook.save()
            return HttpResponse(availbook)
        else:
            return HttpResponse('this is booked already!, Please book into another time slot.')


class bookingView(FormView):
    form_class = availibleFrom
    template_name = 'availibile_form.html'

    def form_valid(self, form):
        data = form.cleaned_data
        room_list = room.objects.filter(catergory=data['room_type'])
        available_room_list = []
        for rooms in room_list:
            if check_availibility(rooms, data['checking_in'], data['checking_out']):
                available_room_list.append(rooms)

        if len(available_room_list) > 0:
            availroom = available_room_list[0]
            availbook = book.objects.create(
                user = self.request.user,
                room = availroom,
                checking_in = data['checking_in'],
                checking_out = data['checking_out'],
            )
            availbook.save()
            return HttpResponse(availbook)
        else:
            return HttpResponse('this is booked already!, Please book into another time slot.')

class CancelBookingView(DeleteView):
    model = book
    success_url = reverse_lazy('Booking:books')