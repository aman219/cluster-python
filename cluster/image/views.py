from django.shortcuts import HttpResponse
from .models import Image
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
@csrf_exempt
def image(reqest):
    if reqest.method == 'POST':
        file = reqest.FILES['file']
        obj = Image.objects.create(image=file, name=file.name[:-4])
        return HttpResponse("success")
    else:
        imgs = Image.objects.all()
        obj = []
        for img in imgs:
            obj.append({"src":img.image.url, "name":img.name})
        return HttpResponse(json.dumps(obj))
