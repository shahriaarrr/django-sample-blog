from django.urls import path
from .views import *

urlpatterns = [
    path('', home),
    path('signup/', signup),
    path('Hi/<str:name>', Hi),
    path("love/<str:name>/<int:number>/", love),
]