from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import SerialNumbers

def index(request):
    latest_jeep_list = SerialNumbers.objects.order_by('-xdatecreated')[:5]
    context = {'latest_jeep_list': latest_jeep_list}
    return render(request, 'g503sn/index.html', context)

# Create your views here.
def detail(request, jeep_id):
    jeep = get_object_or_404(SerialNumbers, pk=jeep_id)
    return render(request, "g503sn/detail.html", {'jeep': jeep})

class JeepListView(generic.ListView):
    model = SerialNumbers
    paginate_by = 25