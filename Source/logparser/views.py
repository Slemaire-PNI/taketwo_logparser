import logparser
from django.http import HttpResponse
from django.shortcuts import redirect
from logparser import logparse
import json

def home(request):
    return redirect('stats')

def stats(request):
    return HttpResponse(json.dumps(logparse.parse(), indent=2))