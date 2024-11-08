from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
def index_main(request):
    return render(request, 'third_task/main_page.html')

def index_shop(request):
    return render(request, 'third_task/shop.html')

def index_trash(request):
    return render(request, 'third_task/trash.html')