from django.shortcuts import render
from django.http import HttpResponse
import random


def home(request):
    return render(request, 'generator/home.html')

def about(request):
    return render(request, 'generator/about.html')
    
def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend (list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('specialcharacter'):
        characters.extend (list('!@#$%^&*()'))

    if request.GET.get('number'):
        characters.extend (list('0123456789'))

    length = int(request.GET.get('length', 14))
    the_password = ''
    for x in range(length):

        the_password += random.choice(characters)

    return render(request, 'generator/password.html', {'password':the_password})
# Create your views here.
