from time import time
from django.shortcuts import HttpResponse
from .models import Video
from django.views.decorators.csrf import csrf_exempt
import json


# Create your views here.
@csrf_exempt
def video(request):
    if request.method == "POST":
        video = request.FILES['file']
        obj = Video.objects.create(video=video, name=video.name[:-4], size = round(video.size/1000000, 2))
        obj.poster_url = "poster"+obj.video.url[:-4]+".jpg"
        obj.save()
        generate_thumbnail("file"+obj.video.url, "file/poster"+obj.video.url[:-4]+".jpg")
        return HttpResponse("success")
    else:
        videos = Video.objects.all()
        obj = []
        for video in videos:
            obj.append({"src":video.poster_url, "name":video.name, "size": video.size, "id": video.id})
        return HttpResponse(json.dumps(obj))

import ffmpeg

def generate_thumbnail(url, out):
    try:
        (
            ffmpeg
            .input(url, ss=1)
            .filter('scale', 1280, 720)
            .output(out, vframes=1)
            .overwrite_output()
            .run(capture_stdout=True, capture_stderr=True)
        )
    except ffmpeg.Error as e:
        print('Error generating thumbnail:', e)

def svideo(request, id):
    video = Video.objects.get(pk=id)
    obj = {"src": video.video.url, "name": video.name, "id":video.id}
    return HttpResponse(json.dumps(obj))

def deleteVideo(request, id):
    video = Video.objects.get(pk=id)
    video.delete();
    return HttpResponse("Deleted Successfully")