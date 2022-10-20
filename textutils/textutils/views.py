#Created by me

from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    #return HttpResponse("Hello Ajay ")
  #  params ={'name':'ajay' ,'place': 'Aurangabad'}
  #  return render(request ,'index.html', params)
      return render(request ,'index.html')
    
def about(request):
    return HttpResponse("About Ajay")

def analyze(request):
    djtext = request.GET.get('text','default')
    removepunc = request.GET.get('removepunc','off')
    extraspaceremover = request.GET.get('extraspaceremover','off')
    newlineremover =request.GET.get('newlineremover','off')
    fullcaps=request.GET.get('fullcaps','off')
    # print(newlineremover)
    params={}
    #return HttpResponse("removepunc")
    if removepunc =="on":
        Punctuation = '''!()-[]{}:;'"\,<>./?@$%^&*-~ '''
        analyzed =""
        for char in djtext:
            if char not in Punctuation:
                analyzed = analyzed + char
            params ={'purpose':'Remove Punctuation','analyzed_text':analyzed}
            djtext =analyzed
        # return render(request ,'analyse.html',params)
    if fullcaps=="on":
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params = {'purpose': 'Change To Uppercase', 'analyzed_text': analyzed}
        djtext=analyzed
        #return render(request, 'analyse.html', params)

    
    elif(extraspaceremover=="on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        # Analyze the text
        djtext =analyzed
        #return render(request, 'analyse.html', params)
    
    elif (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        djtext = analyzed
        # Analyze the text
        #return render(request, 'analyse.html', params)
    
    return render(request, 'analyse.html', params)