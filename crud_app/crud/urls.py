from django.urls import path
from crud.views import person_list, generate_pdf, preview_pdf

urlpatterns = [
    path('', person_list, name='person_list'),
    path('generate-pdf/', generate_pdf, name='generate_pdf'),
    path('preview-pdf/', preview_pdf, name='preview_pdf'),
]