from django.urls import path
from .views import register , loginUser , home ,logoutUser ,detail,listing , ctglisting	,korzinka ,search ,finsh


urlpatterns=[path('register/' , register , name='register' ),
path('login/' , loginUser , name='login' ),
path('' ,home , name='home' ),
path('logout/' ,logoutUser , name='logout' ),
path('detail/<int:ctg>/<int:pk>/' ,detail , name='detail' ),
path('list/<int:pk>/' , listing , name='list' ),
path('ctglist/<int:pk>/' , ctglisting , name='ctglist' ),
path('kor/' , korzinka , name='kor' ),
path('search/' , search , name='search' ),
path('fin/' , finsh , name='finsh' ),
]