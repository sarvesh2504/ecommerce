from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def home(request):
    # Add any necessary logic here
    return render(request, 'ecommerce/index.html')

