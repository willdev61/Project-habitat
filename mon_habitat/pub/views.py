from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .forms import PublicationForm

# Create your views here.
def index(request):
	template = loader.get_template('pub/index.html')
	return HttpResponse(template.render(request=request))


def public(request):
        form = PublicationForm()
        if request.method == 'POST':
            form = PublicationForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
            return HttpResponse('Publication réussie')
        else:
            form = PublicationForm()
        return render(request, 'pub/public.html', {'form':form})