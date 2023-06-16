from django.urls import path
from resume_app import views

app_name = 'resume_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('generate_resume1/', views.generate_resume1, name='generate_resume1'),
    path('generate_resume2/', views.generate_resume2, name='generate_resume2'),
    path('generate_resume3/', views.generate_resume3, name='generate_resume3'),
    path('generate_resume4/', views.generate_resume4, name='generate_resume4'),
    path('generate_resume5/', views.generate_resume5, name='generate_resume5'),
    path('generate_resume6/', views.generate_resume6, name='generate_resume6'),
    path('generate_resume7/', views.generate_resume7, name='generate_resume7'),
    path('generate_resume8/', views.generate_resume8, name='generate_resume8'),
    path('generate_resume9/', views.generate_resume9, name='generate_resume9'),
    path('generate_resume10/', views.generate_resume10, name='generate_resume10'),
    path('generate_resume11/', views.generate_resume11, name='generate_resume11'),
    path('generate_resume12/', views.generate_resume12, name='generate_resume12'),
    path('generate_resume13/', views.generate_resume13, name='generate_resume13'),
    path('generate_resume14/', views.generate_resume14, name='generate_resume14'),
    path('generate_resume15/', views.generate_resume15, name='generate_resume15'),
]
