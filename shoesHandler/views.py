from django.shortcuts import render
from django.http import HttpResponse, Http404
from shoesHandler.models import Shoes

# Create your views here.

def home(request):
    if request.method == 'GET':
        return render(request, 'inventory/home.html')
    elif request.method == 'POST':
        return HttpResponse('you posted something!')



def shoesByMark(request,mark):
    try:
        shoes = Shoes.objects.filter(mark = mark)
    except Shoes.DoesNotExist:
        raise Http404("that item does not exist!")
    return render(request,'inventory/shoesGrid.html',{
        'shoes': shoes,
    })

def shoesByCategory(request,category,pageNumber):
    limit = int(pageNumber)
    limit =  limit * 4
    try:

        shoesOfTheCategory = Shoes.objects.filter(category= category)[limit:(limit + 4)]
        pagesNumber = len(Shoes.objects.filter(category= category)) / 4
    except Shoes.DoesNotExist:
        raise Http404('that item does not exist!')
    return render(request,'inventory/category.html', {
        'shoes': shoesOfTheCategory,
        'limit': limit,
        'category':category,
        'pagesNumber': int(pagesNumber) + 1
         })

