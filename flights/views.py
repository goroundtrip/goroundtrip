from django.shortcuts import render, get_object_or_404, redirect
from .models import Flight, Booking
from .forms import BookingForm

# Show list of all available flights
def flight_list(request):
    flights = Flight.objects.all()
    return render(request, 'flights/index.html', {'flights': flights})

# Book a specific flight
def book_flight(request, flight_id):
    flight = get_object_or_404(Flight, id=flight_id)

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.flight = flight
            booking.save()
            return render(request, 'flights/booking_success.html', {'booking': booking})
    else:
        form = BookingForm()

    return render(request, 'flights/book_flight.html', {
        'flight': flight,
        'form': form
    })
