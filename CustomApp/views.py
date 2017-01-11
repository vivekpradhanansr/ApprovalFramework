from django.shortcuts import render
from constants import WORKFLOW_APPS, REQUEST_IDENTIFIER
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from serializers import TransactionsSerializer
from django.http import Http404
from django.contrib.auth.models import User

from helpers import get_request_params, flow_config


# Create your views here.
def process(request):
    return render(request, 'landingpage.html', {'taskprocess': WORKFLOW_APPS})


class ProcessListView(generics.ListAPIView):

    def list(self, request, **kwargs):
        import ipdb; ipdb.set_trace()
        app_title = get_request_params('app_name', self.request, **kwargs)
        config = flow_config(app_title)
        model = config.PROCESS[config.INITIAL]['model']().title
        queryset = User.objects.all()
        serializer = TransactionsSerializer(queryset, many=True)
        return Response(serializer.data)


class StartProcess(APIView):

    def get(self, request, **kwargs):
        serializer = request.user.id
        return Response(serializer.data)

    def post(self, request, **kwargs):
        return Response("", status.HTTP_201_CREATED)

class UpdateProcess(APIView):

    def get(self, request, **kwargs):
        return True

    def post(self, request, **kwargs):
        return False


class ProcessUpdate(APIView):

    def get_object(self, pk, **kwargs):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk, **kwargs):
        activity = self.get_object(pk)
        serializer = TransactionsSerializer(activity)
        return Response(serializer.data)

    def put(self, request, pk, **kwargs):
        activity = self.get_object(pk)
        serializer = TransactionsSerializer(activity, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, **kwargs):
        activity = self.get_object(pk)
        activity.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)









