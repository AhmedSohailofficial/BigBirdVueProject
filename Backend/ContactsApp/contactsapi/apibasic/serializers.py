from rest_framework import serializers
from .models import SecondProducts

class SecondProductsSerializer(serializers.ModelSerializer):
	class Meta:
		model = SecondProducts
		fields ='__all__'