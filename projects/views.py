from django.core.exceptions import ObjectDoesNotExist
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

from .models import *
from .serializer import *

@api_view(['GET'])
def get_project(request, name, format=None):
    try:
        project = Project.objects.get(name=name)
    except ObjectDoesNotExist:
        return Response({ 'error': 'Project not found.' }, status=status.HTTP_404_NOT_FOUND)
    
    serializer = ProjectSerializer(project)
    return Response(serializer.data)
