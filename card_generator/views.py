from django.shortcuts import render, redirect, get_object_or_404
from .models import Participant
# Create your views here.
def index(request):
    return render(request, 'card_generator/home.html')

def generate(request):
    if request.method == 'POST':
        full_name = clean_input(request.POST.get('full_name'))
        phone_number = clean_input(request.POST.get('phone_number'))
        dance_category = clean_input(request.POST.get('dance_category'))
        age = clean_input(request.POST.get('age'))

        if Participant.objects.filter(full_name=full_name).exists() or Participant.objects.filter(phone_number=phone_number).exists():
            user = Participant.objects.filter(full_name=full_name).first()
            return render(request, 'card_generator/card.html', {'user': user})

        # Redirect to a success page or render a template
        return render(request, 'card_generator/home.html')  # replace with the name of your success URL
    return render(request, 'card_generator/home.html')  # Render the form template

def clean_input(value):
    if value:
        return value.lower().replace(' ', '')
    return value