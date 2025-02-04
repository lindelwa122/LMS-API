from rest_framework import status
from rest_framework.response import Response

from .models import *
from .serializer import *

def get_project(request, name, format=None):
    project = Project.objects.get(name=name)
    if not project:
        return Response({ 'error': 'Project not found.' }, status=status.HTTP_404_NOT_FOUND)
    
    serializer = ProjectSerializer(project)
    return Response(serializer.data)
