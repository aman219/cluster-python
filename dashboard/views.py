from django.shortcuts import HttpResponse
import shutil
import json
import os
# Create your views here.

def home(request):
    return HttpResponse("Home")

def dashboard(request):
    size = shutil.disk_usage(os.path.expanduser("~"))
    dash = {
        "total": size.total,
        "used": size.used,
        "free": size.free
    }
    dash = json.dumps(dash)
    return HttpResponse(dash)