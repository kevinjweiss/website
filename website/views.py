from django.shortcuts import render
from website.models import Index

# Create your views here.
def index(request):
    bla = Index.objects.all()
    context = {
        'index': bla
    }
    return render(request, 'index.html', context=context)