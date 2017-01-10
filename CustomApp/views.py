from django.shortcuts import render
from constants import TASKPROCESS_APP


# Create your views here.
def taskprocess(request):
    return render(request, 'landingpage.html', {'taskprocess': TASKPROCESS_APP})
