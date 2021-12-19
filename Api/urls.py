from django.urls import path
from .views import CtgModelApi ,CtgTypeModelApi ,ProductModelApi ,account_GetVeiw ,product_one_GetVeiw ,KarzinkaModelApi



urlpatterns=[path('api/', CtgModelApi.as_view(), name='ctg'),
path('api/ctgtype/', CtgTypeModelApi.as_view(),name='ctgType'),
path('api/product/', ProductModelApi.as_view(),name='product_api'),
path('api/pag/', account_GetVeiw,name='pag'),
path('api/product_one/<int:pk>/', product_one_GetVeiw ,name='one_produck'),
path('api/karzinka', KarzinkaModelApi.as_view() ,name='karzinka'),
]