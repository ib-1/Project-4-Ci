from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, FormView, View
from .models import room, book
from .forms import availibleFrom
from Booking.book_functions.availibility import check_availibility
# Create your views here.

class rooms(ListView):
    model = room

class books(ListView):
    model = book


class roomdetailview(View):
    def get(self, request, *args, **kwargs):
        room_category = self.kwargs.get('category', None)
        # room_list = room.objects.filter(category=category)
        context = {
            "room_category": room_category
        }
        return render(request, 'roomdetailview.html', context)


    def post(self, request, *args, **kwargs):
        room_list = room.objects.filter(category=category)
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