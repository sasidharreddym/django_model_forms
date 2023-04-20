from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse

# Create your views here.

def insert_topic(request):
    TFO=TopicForm()
    d={'TFO':TFO}

    if request.method=='POST':
        TFDO=TopicForm(request.POST)
        if TFDO.is_valid():
            TFDO.save()
            return HttpResponse('topic insertd successfully')

    return render(request,'insert_topic.html',d)



def insert_webpage(request):
    WFO=WebpageForm()
    d={'WFO':WFO}
    if request.method=='POST':
        WFDO=WebpageForm(request.POST)
        if WFDO.is_valid():
            WFDO.save()
            return HttpResponse('webpage insertion is successfull')

    return render(request,'insert_webpage.html',d)
    

def insert_accessrecord(request):
    ARFO=AccessRecordForm()
    d={'ARFO':ARFO}
    if request.method=='POST':
        ARFDO=AccessRecordForm(request.POST)
        if ARFDO.is_valid:
            ARFDO.save()
            return HttpResponse('inserted access record data successfully')
        
    return render(request,'insert_accessrecord.html',d)













