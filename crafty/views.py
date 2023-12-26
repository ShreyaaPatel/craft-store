from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Create your views here.
def index(request):
    pb = Product.objects.all()
    return render(request, "index.html", context={"pb":pb})
    