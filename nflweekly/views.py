from django.shortcuts import render
from nflweekly.models import Week

# Create your views here.
def weekly_index(request):
    weeks = Week.objects.all()
    
    context = {
        'weeks': weeks,
    }
    return render(request, 'nflweekly_index.html', context)

def weekly_detail(request, pk):
    week = Week.objects.get(pk=pk)
    context = {
        'week': week,
    }
    return render(request, 'nflweekly_detail.html', context)
