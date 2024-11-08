from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
def index_main(request):
    return render(request, 'fourth_task/main_page.html')

def index_shop(request):
    flowers = ['Орхидеи', 'Гортензии', 'Тюльпаны']
    context = {
        'flowers': flowers
    }
    return render(request, 'fourth_task/shop.html', context)

def index_trash(request):
    return render(request, 'fourth_task/trash.html')