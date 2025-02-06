from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import *

urlpatterns = [
    path('get/<str:name>', get_project, name='get_project'),
    path('submit', update_grade, name='update_grade')
]

urlpatterns = format_suffix_patterns(urlpatterns)
