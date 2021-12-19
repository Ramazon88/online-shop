from rest_framework import serializers
from account.models import *

class CtgModelSerialzer(serializers.ModelSerializer):
	class Meta:
		model=CtgModel
		fields='__all__'
class CtgTypeModelSerialzer(serializers.ModelSerializer):
	class Meta:
		model=CtgTypeModel
		fields='__all__'		
class ProductModelSerialzer(serializers.ModelSerializer):
	class Meta:
		model=ProductModel
		fields='__all__'				
class KarzinkaModelSerialzer(serializers.ModelSerializer):
	class Meta:
		model=Karzinka
		fields='__all__'						
