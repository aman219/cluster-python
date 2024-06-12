from time import timezone
from django.shortcuts import HttpResponse
from .models import Audio
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
@csrf_exempt
def audio(reqest):
    if reqest.method == 'POST':
        file = reqest.FILES["file"]
        obj = Audio.objects.create(audio_file=file, name=file.name[:-4])
        obj.save()
        return HttpResponse("uploaded successfully..")
    else:
        audios = Audio.objects.all()
        obj = []
        for audio in audios:
            obj.append({"id": audio.id, "name": audio.name}) 
        return HttpResponse(json.dumps(obj))

def paly(reqest, id):
    audio = Audio.objects.get(pk=id)
    obj = {"name": audio.name, "src":audio.audio_file.url, "id":audio.id}
    return HttpResponse(json.dumps(obj))

def deleteAudio(request, id):
    audio = Audio.objects.get(pk=id)
    audio.delete()
    return HttpResponse("Successfully deleted audio")