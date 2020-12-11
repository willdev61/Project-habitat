from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .forms import PublicationForm
from .models import Publication
from .filters import PublicationFilter


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


def detail(request, publication_id):
    publication = get_object_or_404(Publication, pk=publication_id)
    context = {
        'first_name' : publication.first_name,
        'last_name' : publication.last_name,
        'agency_name' : publication.agency_name,
        'cities' : publication.cities,
        'categories' : publication.categories,
        'status' : publication.status,
        'number_1' : publication.number_1,
        'number_2' : publication.number_2,
        'description' : publication.description,
        'image' : publication.image_one,
    }
    return render(request, 'pub/detail.html', context)



def search(request):
    f = PublicationFilter(request.GET, queryset=Publication.objects.all())
    context = {
        'filter': f
    }
    return render(request, 'pub/search.html', context)