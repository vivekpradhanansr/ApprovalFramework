from django.shortcuts import render
from constants import TASKPROCESS_APP
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

from helpers import get_request_params


# Create your views here.
def process(request):
    return render(request, 'landingpage.html', {'taskprocess': TASKPROCESS_APP})


class ProcessListView(generics.ListAPIView):

    def get_queryset(self, **kwargs):
        user = self.request.user
        app_title = get_request_params('app_name',self.request, **kwargs)
        return app_title


class ProcessStart(APIView):

    def get(self, request, **kwargs):
        serializer = request.user.id
        return Response(serializer.data)

    def post(self, request, **kwargs):
        return Response("", status.HTTP_201_CREATED)






