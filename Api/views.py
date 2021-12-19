from django.shortcuts import render
from rest_framework import generics
from account.models import * 
from .serializers import CtgModelSerialzer ,CtgTypeModelSerialzer ,ProductModelSerialzer ,KarzinkaModelSerialzer
from rest_framework.filters import	SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.
from .paginations import CustomPagination , StandardResultsSetPagination
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.paginator import Paginator
from rest_framework import status

class CtgModelApi(generics.ListCreateAPIView):
	queryset=CtgModel.objects.all()
	serializer_class=CtgModelSerialzer

class CtgTypeModelApi(generics.ListCreateAPIView):
	queryset=CtgTypeModel.objects.all()
	serializer_class=CtgTypeModelSerialzer
	


# class ProductModelApi(generics.ListCreateAPIView):

# 	queryset=ProductModel.objects.all()
# 	serializer_class=ProductModelSerialzer
# 	filter_backends=(DjangoFilterBackend , SearchFilter)
# 	filter_fields=('ctgType',)
@api_view(['GET',])
def account_GetVeiw(request ):
	if request.method=='GET' and request.GET.get('page_n'):
		a=int(request.GET.get('page_n'))
		queryset=ProductModel.objects.all()
		paginator = Paginator(queryset, 2) # Show 25 contacts per page.		
		page_obj = paginator.get_page(a)
		
	elif request.method=='GET' and request.GET.get('page_p'):
		a=int(request.GET.get('page_p'))
		queryset=ProductModel.objects.all()
		paginator = Paginator(queryset, 2) # Show 25 contacts per page.		
		page_obj = paginator.get_page(a)
	else:
		queryset=ProductModel.objects.all()
		paginator = Paginator(queryset, 2) # Show 25 contacts per page.		
		page_obj = paginator.get_page(1)

	serializer=ProductModelSerialzer(page_obj , many=True)
	
	return Response(serializer.data )
class ProductModelApi(generics.ListCreateAPIView):
	pagination_class=StandardResultsSetPagination
	queryset=ProductModel.objects.all()
	serializer_class=ProductModelSerialzer	
@api_view(['GET',])
def product_one_GetVeiw(request , pk):
	try:
		ac=ProductModel.objects.get(id=pk)	
	except:
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method=='GET':
		serializer=ProductModelSerialzer(ac)
		return Response(serializer.data)				
class KarzinkaModelApi(generics.ListCreateAPIView):
	queryset=Karzinka.objects.all()
	serializer_class=KarzinkaModelSerialzer
		