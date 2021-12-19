from django.shortcuts import render , redirect
from .forms import UserForm
from django.contrib import messages
# Create your views here.
from django.contrib.auth import authenticate , login ,logout
from django.contrib.auth.decorators import login_required
from .models import *
from django.core.paginator import Paginator
from django.db.models import Q

def register(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:	
		form = UserForm()
		if request.method == 'POST':
			form = UserForm(request.POST)
			if form.is_valid():
				form.save()
				user= form.cleaned_data.get('username')
				messages.success(request , 'accoun yaratildi'+' '+user)
				return redirect('login')


		context={'form':form}	
		return render(request , 'register.html' , context)	
def loginUser(request ):
	if request.user.is_authenticated:
		print('---',request.user)
		return redirect('home')
	else:	
		if request.method == 'POST':
			username=request.POST.get('username')
			password=request.POST.get('password')

			user=authenticate(request , username=username , password=password)

			if user is not None:
				login(request ,user)
				return redirect('home')
			else:
				messages.info(request	, 'password or username incorrect ?')
				 
		context={}
		return render(request, 'login.html', context)
	
def logoutUser(request):
	logout(request)
	return redirect('login')
#@login_required(login_url='login')	
def home(request ):
	if request.POST:
		
		if request.user.is_authenticated:
			maxsulot=request.POST.get("product_id")
			is_costumer=True
			take_p=ProductModel.objects.get(id=int(maxsulot))
			try :
				filters=Karzinka.objects.get(title_k=take_p.title)
			except:
				filters=None	
			if filters and filters.is_delier == True :
				filters.soni+=1
				filters.total_cost=filters.price_k*filters.soni	
				filters.save()
			else :	
				kor=Karzinka()
				kor.title_k= take_p.title  
				kor.image_k=take_p.image   
				kor.price_k=take_p.price   
				kor.username = request.user
				kor.catrgory_k=take_p.ctgType
				kor.is_delier=True 
				kor.total_cost = take_p.price
				kor.soni=1
				kor.save()    
		else:
			is_costumer=False	
			return	redirect('login')
	else:
		take_p=''		
		is_costumer=False			
	a=CtgModel.objects.all()
	b=CtgTypeModel.objects.all()
	c=ProductModel.objects.all().order_by('-id')



	
	context={'ctgs':a,'ctgType':b , 'product_all':c ,'is_costumer':is_costumer	, 'take_p':take_p}
	return render(request, 'index.html',context)	
def detail(request ,pk , ctg ):
	if request.POST:
		
		if request.user.is_authenticated:
			maxsulot=request.POST.get("product_id")
			is_costumer=True
			take_p=ProductModel.objects.get(id=int(maxsulot))
			try :
				filters=Karzinka.objects.get(title_k=take_p.title)
			except:
				filters=None	
			if filters and filters.is_delier == True :
				filters.soni+=1
				filters.total_cost=filters.price_k*filters.soni	
				filters.save()
			else :	
				kor=Karzinka()
				kor.title_k= take_p.title  
				kor.image_k=take_p.image   
				kor.price_k=take_p.price   
				kor.username = request.user
				kor.catrgory_k=take_p.ctgType
				kor.is_delier=True 
				kor.total_cost = take_p.price
				kor.soni=1
				kor.save()    
		else:
			is_costumer=False	
			return	redirect('login')
	else:
		take_p=''		
		is_costumer=False		
	a=CtgModel.objects.all()
	b=CtgTypeModel.objects.all()
	c=ProductModel.objects.all().order_by('-id')
	one=ProductModel.objects.get(id=pk)

	print('---' , one)
	context={'ctgs':a,'ctgType':b , 'product_all':c , 'one':one,'is_costumer':is_costumer	, 'take_p':take_p}
	return render(request, 'detail.html',context)		

def listing(request , pk):
	if request.POST:
		page_number=1
		if request.user.is_authenticated:
			maxsulot=request.POST.get("product_id")
			is_costumer=True
			take_p=ProductModel.objects.get(id=int(maxsulot))
			try :
				filters=Karzinka.objects.get(title_k=take_p.title)
			except:
				filters=None	
			if filters and filters.is_delier == True :
				filters.soni+=1
				filters.total_cost=filters.price_k*filters.soni	
				filters.save()
			else :	
				kor=Karzinka()
				kor.title_k= take_p.title  
				kor.image_k=take_p.image   
				kor.price_k=take_p.price   
				kor.username = request.user
				kor.catrgory_k=take_p.ctgType
				kor.is_delier=True 
				kor.total_cost = take_p.price
				kor.soni=1
				kor.save()    
		else:
			is_costumer=False	
			return	redirect('login')
	
	elif request.GET: 
		page_number = request.GET.get('page')
		is_costumer=False
		take_p=''
	
	elif not request.POST and not request.GET: 
		page_number = 1
		take_p=''		
		is_costumer=False


	contact_list = ProductModel.objects.filter(ctgType_id=pk)
	a=CtgModel.objects.all()
	b=CtgTypeModel.objects.all()
	paginator = Paginator(contact_list, 10) # Show 25 contacts per page.		
	page_obj = paginator.get_page(page_number)
	
	return render(request, 'list.html', {'page_obj': page_obj ,'ctgs':a,'ctgType':b , 
		'p':paginator ,'activ':int(page_number),'is_costumer':is_costumer	, 'take_p':take_p })	
def ctglisting(request , pk):
	if request.POST:
		page_number=1
		if request.user.is_authenticated:
			maxsulot=request.POST.get("product_id")
			is_costumer=True
			take_p=ProductModel.objects.get(id=int(maxsulot))
			try :
				filters=Karzinka.objects.get(title_k=take_p.title)
			except:
				filters=None	
			if filters and filters.is_delier == True :
				filters.soni+=1
				filters.total_cost=filters.price_k*filters.soni	
				filters.save()
			else :	
				kor=Karzinka()
				kor.title_k= take_p.title  
				kor.image_k=take_p.image   
				kor.price_k=take_p.price   
				kor.username = request.user
				kor.catrgory_k=take_p.ctgType
				kor.is_delier=True 
				kor.total_cost = take_p.price
				kor.soni=1
				kor.save()    
		else:
			is_costumer=False	
			return	redirect('login')
	
	elif request.GET: 
		page_number = request.GET.get('page')
		is_costumer=False
		take_p=''
	
	elif not request.POST and not request.GET: 
		page_number = 1
		take_p=''		
		is_costumer=False

	a=CtgModel.objects.all()
	b=CtgTypeModel.objects.all()
	d=CtgTypeModel.objects.filter(ctg_id=pk)

	
	if d:
		s=""
		for i in d:
			if (d[len(d)-1]).id == i.id:
				s+=f'(ctgType_id="{i.id}")'
			else:	
				s+=f'(ctgType_id="{i.id}")or'
	else :
		s="ctgType_id=0"
	print('??????' ,s)
	contact_list = ProductModel.objects.raw	(f""" SELECT account_productmodel.id , account_productmodel.image ,account_productmodel.image1,
account_productmodel.image2,account_productmodel.image3,account_productmodel.text ,
account_productmodel.price ,account_productmodel.is_active ,account_productmodel.brand FROM
account_productmodel WHERE {s} """)
	if contact_list :
		paginator = Paginator(contact_list, 2) # Show 25 contacts per page.
		if request.GET: 
			page_number = request.GET.get('page')
		else :
			page_number=1	
		page_obj = paginator.get_page(page_number)
		
		return render(request, 'list.html', {'page_obj': page_obj ,'ctgs':a,'ctgType':b ,
		 'p':paginator ,'activ':int(page_number),'is_costumer':is_costumer	, 'take_p':take_p})		
		
	else:
		return render(request, 'not_list.html', { 'ctgs':a,'ctgType':b })
@login_required(login_url='login')						
def korzinka(request):
	c=Karzinka.objects.filter(username=request.user)
	sotildi=False
	summa=0	
	if request.POST :
		ids=request.POST.get('product_delete')
		
		try:
			n=Karzinka.objects.get(id=ids)
			n.delete()
		except:
			pass
	elif request.GET :
		sotildi=True
		summa=request.GET.get('all_sum')
		for i in c:
			if request.GET.get(f'n{i.id}') :
				i.soni=int(request.GET.get(f'n{i.id}'))
				i.total_cost=i.soni	* i.price_k	
				i.save()

	a=CtgModel.objects.all()
	b=CtgTypeModel.objects.all()
	
	return render(request, 'product_summary.html', { 'ctgs':a,'ctgType':b , 'porduct_pay':c ,'sotildi':sotildi,'summa':summa})


def search(request):
	
	if request.GET :
		word=request.GET.get('word')
		search=ProductModel.objects.filter(title__contains=word).all()[:20]
	else:
		return redirect('home')	
	a=CtgModel.objects.all()
	b=CtgTypeModel.objects.all()
	
	return render(request , 'products.html', { 'ctgs':a,'ctgType':b , 'search':search ,
		'len':len(search)})


def finsh(request):
	if request.POST:
		c=Karzinka.objects.filter(username=request.user)
		clients=ClientModel()
		phone=request.POST.get('phone')
		mobile=request.POST.get('mobile')
		clients.phone=phone
		clients.mobile=mobile
		clients.user_client=request.user
		clients.save()
		for i in c:
			i.is_delier	= False	
			i.save()

	return redirect('home')