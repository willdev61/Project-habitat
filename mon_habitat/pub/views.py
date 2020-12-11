from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .forms import PublicationForm
from .models import Publication


# Create your views here.
def index(request):
	return render(request, 'pub/index.html')


def public(request):
    if request.method == "POST":
        form = PublicationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'pub/succees.html')
    else:
        form = PublicationForm()
    return render(request, 'pub/public.html', {'form':form})



def listing(request):
    publications = Publication.objects.all().order_by('-made_at')
    context = {
        'publications' : publications
    }
    return render(request, 'pub/listing.html', context)