from django.shortcuts import render , redirect
from .models import Room
from django.shortcuts import get_object_or_404

# Create your views here.
def index(request):
    rooms = Room.objects.all()
    return render(request, 'home.html', {'rooms': rooms})

def add_room(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        contact = request.POST.get('contact')
        image = request.FILES.get('image')
        description = request.POST.get('description')
        price = request.POST.get('price')
        location = request.POST.get('location')

        Room.objects.create(
            name=name,
            contact=contact,
            description=description,
            price=price,
            location=location,
            image=image
        )
        return redirect('home')
    return render(request, 'add_room.html')
def room_detail_view(request, pk):
    # Fetch the specific room from the database using its primary key (pk)
    # If not found, it will automatically return a 404 error
    room = get_object_or_404(Room, pk=pk)
    
    # Pass the single room object to the template
    context = {
        'room': room
    }
    return render(request, 'room.html', context)

def about(request):
    return render(request, 'about.html')