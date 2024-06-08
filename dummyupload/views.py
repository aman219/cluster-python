from django.shortcuts import HttpResponse
from .models import File
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def upload(request):
    if request.method == 'POST':
        file = request.FILES['file']
        File.objects.create(file=file, name="testing")
        return HttpResponse('scussuce')
    else:
        return HttpResponse("working")