from django.urls import path
from . import views

urlpatterns = [
	
	path('SecondProducts/', views.SecondProductsList, name="SecondProducts_List"),
	
]
