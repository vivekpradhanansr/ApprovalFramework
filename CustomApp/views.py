from django.shortcuts import render
from constants import WORKFLOW_APPS
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from django.http import Http404
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework.renderers import TemplateHTMLRenderer


from models import get_app_detail, get_queryset


def process(request):
    return render(request, 'templates/landingpage.html', {'taskprocess': WORKFLOW_APPS})


class ProcessListView(generics.ListAPIView, LoginRequiredMixin):

    def list(self, request, **kwargs):
        config = get_app_detail(request, **kwargs)
        model = config.PROCESS[config.INITIAL]['model']
        serializer = config.PROCESS[config.INITIAL]['serializer']
        self.queryset = queryset = model.objects.filter(is_active=True).exclude(process_status='Completed',
                                                                                request_status__in=['Completed',
                                                                                                    'Rolled Back'])
        serializer = serializer(queryset, many=True)
        return Response(serializer.data)


class StartProcess(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'templates/process_form.html'

    def get(self, request, **kwargs):
        config = get_app_detail(request, **kwargs)
        serializer = config.PROCESS[config.INITIAL]['serializer']
        return Response({'serializer': serializer()})

    def post(self, request, **kwargs):
        config = get_app_detail(request, **kwargs)
        process_serializer = config.PROCESS[config.INITIAL]['serializer']
        serializer = process_serializer(data=request.data)
        if serializer.is_valid():
            serializer.saveas(request)
            return Response({'serializer': serializer}, status.HTTP_201_CREATED)
        return Response(status.HTTP_400_BAD_REQUEST)


class ProcessUpdate(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'templates/process_update.html'

    def get_object(self, request, pk, **kwargs):
        try:
            config = get_app_detail(request, **kwargs)
            model = config.PROCESS[config.INITIAL]['model']
            return get_object_or_404(model, pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk, **kwargs):
        config = get_app_detail(request, **kwargs)
        process_serializer = config.PROCESS[config.INITIAL]['serializer']
        activity = self.get_object(request, pk, **kwargs)
        serializer = process_serializer(activity)
        return Response({'serializer': serializer, 'pk': pk})

    def post(self, request, pk, **kwargs):
        config = get_app_detail(request, **kwargs)
        process_serializer = config.PROCESS[config.INITIAL]['serializer']
        activity = self.get_object(request, pk, **kwargs)
        serializer = process_serializer(activity, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'serializer': serializer, 'pk': pk})
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, **kwargs):
        activity = self.get_object(request, pk, **kwargs)
        activity.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ApproveListView(generics.ListAPIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'templates/approval.html'

    def list(self, request, **kwargs):
        config = get_app_detail(request, **kwargs)
        serializer = config.PROCESS[config.INITIAL]['serializer']
        self.queryset = queryset = get_queryset(request, **kwargs)
        serializer = serializer(queryset, many=True)
        return Response(serializer.data)











