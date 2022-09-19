from django.shortcuts import HttpResponse
from .models import File
from django.views.decorators.csrf import csrf_exempt
import shutil
import json

# Create your views here.

@csrf_exempt
def upload(request):
    if request.method == 'POST':
        file = request.FILES['file']
        File.objects.create(file=file, name="testing")
        return HttpResponse('scussuce')
    else:
        return HttpResponse("working")

def dashboard(request):
    size = shutil.disk_usage("/home/aman")
    dash = {
        "total": size.total,
        "used": size.used,
        "free": size.free
    }
    dash = json.dumps(dash)
    return HttpResponse(dash)