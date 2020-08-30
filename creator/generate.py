from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.decorators import login_required

from .models import *
from pptx import Presentation


@login_required
def next(request,pk):
    obj = pitchDeck.objects.get(pitchDeckId=pk)
    prs = Presentation()
    title_slide_layout = prs.slide_layouts[0]
    slide = prs.slides.add_slide(title_slide_layout)
    title = slide.shapes.title
    subtitle = slide.placeholders[1]

    title.text = obj.startupName
    subtitle.text = "python-pptx was here!"

    prs.save(obj.startupName+".pptx")
    return render(request,'generate.html',{'obj':obj})

