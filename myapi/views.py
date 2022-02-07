from django.shortcuts import render
from rest_framework import viewsets
from .serializers import StatusSerializer, InstallationSerializer
from .models import Installation, Status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


class InstallationViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = Installation.objects.all().order_by('date_modified');
        serializer = InstallationSerializer(queryset, many = True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Installation.objects.all()
        installation = get_object_or_404(queryset, pk=pk)
        serializer = InstallationSerializer(installation)
        return Response(serializer.data)

    def create(self, request):
        serializer = InstallationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            installation = serializer.save()
        
        return Response(serializer.data)

    def update(self, request, pk=None):
        serializer = StatusSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            status = serializer.save()
        
        return Response(serializer.data)


class StatusViewSet(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

