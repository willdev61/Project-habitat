from django.http import HttpResponse

# Create your views here.
def index(request):
	message = "Hello this is my first app"
	return HttpResponse(message)