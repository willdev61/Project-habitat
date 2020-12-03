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
            form = PublicationForm(request.POST or None, request.FILES or None)
            if form.is_valid():
                form.save()
                messages.success(request, 'Your password was updated successfully!')
            return HttpResponse('Publication réussie')
        else:
            form = PublicationForm()
        
        return render(request, 'pub/public.html', {'form':form})