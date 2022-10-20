import datetime as dt
import os
import shutil

from django.shortcuts import redirect, render
from gtts import gTTS
from playsound import playsound


# Create your views here.
def home(request):

	return render(request,'index.html')

def text(request):
	usertext = ''
	if request.method == 'POST':
		usertext = request.POST.get('usertext')
		audio = 'media/speech.mp3'
		language = 'en'
		sp = gTTS(text=usertext, tld='co.in',  lang=language, slow=False)
		sp.save(audio)
		return render(request,'download.html',{'data':audio})
	else:

		return render(request,'text.html')


def download(request):
	os.replace()
	return render(request,'download.html')

def video(request):
	return render(request,'video.html')
