from django.urls import path
from . import views
from .views import *


urlpatterns = [
    path('', views.login, name='login'),
    path('register/', views.voterRegister, name='voterRegister'),
    path('dashboardVoter/<str:id>/', views.dashborardVoter, name='dashboardVoter'),
    path('verifyVote/<str:id>/<str:election_id>/<str:candidate_id>/<str:key>/', views.verifyVote, name='verifyVote'),
    path('dashboardAdmin/<str:id>/', views.dashboardAdmin, name='dashboardAdmin'),
    path('createNew/<str:pk>/', views.createNew, name='createNew'),
    path('all_candidate/<str:region_id>/', views.all_candidate, name='all_candidate'),
    path('voterLogin/', views.voterLogin, name='voterLogin'),
    path('adminLogin/', views.adminLogin, name='adminLogin'),
    path('winner/<str:id>/', views.winner, name='winner'),
]