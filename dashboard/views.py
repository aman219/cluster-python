from django.shortcuts import HttpResponse
import shutil
import json
import os
# Create your views here.

arr = [0,25,35,84,65,48,87]

def home(request):
    return HttpResponse("Home")

def dashboard(request):
    size = shutil.disk_usage(os.path.expanduser("~"))
    arr[0] += 1
    dash = {
        "total": size.total,
        "used": size.used,
        "free": size.free,
        "beam": arr
    }
    dash = json.dumps(dash)
    return HttpResponse(dash)