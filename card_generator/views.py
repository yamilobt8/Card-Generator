import gspread
from google.oauth2.service_account import Credentials
from django.shortcuts import render
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
scopes = [
    'https://www.googleapis.com/auth/spreadsheets',
]

credentials_path = os.path.join(BASE_DIR, 'card_generator', 'credentials.json') # credentials.json path
credentials = Credentials.from_service_account_file(credentials_path, scopes=scopes)
client = gspread.authorize(credentials)
sheet_id = "Your_sheet_id" # Replace with your sheet_id
sheet = client.open_by_key(sheet_id)
values_list = sheet.sheet1.get_all_values()
def index(request):
    return render(request, 'card_generator/home.html')

def generate(request):
    if request.method == 'POST':
        full_name = clean(request.POST.get('full_name'))
        phone_number = clean(request.POST.get('phone_number'))
        dance_category = clean(request.POST.get('dance_category'))
        age = clean(request.POST.get('age'))
        for candidat in values_list:
            if clean(candidat[2]) == full_name:
                print('candidat found')
                print('generating card .......')
                return render(request, 'card_generator/card.html', {
                    'username': candidat[2],
                    'phone': candidat[7],
                    'email': candidat[1],
                    'dance_type': candidat[5],
                    'profile_picture_url': "https://avatars.githubusercontent.com/u/123247514?v=4"
                })
        return render(request, 'card_generator/home.html')  # replace with the name of your success URL
    return render(request, 'card_generator/home.html')  # Render the form template

def clean(value):
    if value:
        return value.lower().replace(' ', '')
    return value