from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.
def home(request):
    passtr="sdfsd"
    return render(request,'generator/home.html',)
def password1(request):
    length= int(request.GET.get('Length',7))
    uppercase=request.GET.get('Uppercase',True)
    Special_characters = request.GET.get('Specialcharacers', True)
    Numbers=request.GET.get('Numbers', True)
    characters=list('abcdefghijklmnopqrstuvwxyz')
    if Numbers: characters.extend(list('1234567890'))
    if uppercase: characters.extend(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
    if Special_characters: characters.extend(list('*&^%$#@'))
    thispasswrd=''
    for i in range(length):
        thispasswrd+=random.choice(characters)
    return render(request, 'generator/password.html',{'password':thispasswrd} )

def about_page(request):
    return render(request, 'generator/about_page.html')