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


@api_view(['POST'])
def update_grade(request, format=None):
    username = request.data['username']
    score = request.data['grade']
    project_id = request.data['project_id']
    
    # Try to get project
    try:
        project = Project.objects.get(name=project_id)
    except ObjectDoesNotExist:
        return Response({ 'error': 'Project not found.' }, status=status.HTTP_404_NOT_FOUND)

    student, _ = Student.objects.get_or_create(username=username)
        
    try:
        grade = Grade.objects.get(student=student, project=project)
        
        # Only update grade if the new score is better than the previous one
        if grade.score < score:
            grade.objects.update(score=score)
            grade.save()
            
    except ObjectDoesNotExist:
        grade = Grade.objects.create(student=student, project=project, score=score)
        grade.save()
