from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import SecondProductsSerializer
from .models import SecondProducts
# Create your views here.

@api_view(['GET'])
def SecondProductsList(request):
	SecondProductsArray = SecondProducts.objects.all().order_by('id')
	serializer = SecondProductsSerializer(SecondProductsArray, many=True)
	return Response(serializer.data)
