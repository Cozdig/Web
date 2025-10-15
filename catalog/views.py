from django.shortcuts import render

# Create your views here.
def home_page(request):
    return render(request, 'home.html')

def contacts_page(request):
    return render(request, 'contacts.html')