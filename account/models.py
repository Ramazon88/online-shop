from django.db import models

# Create your models here.
class CtgModel(models.Model):
	name = models.CharField(max_length=250)
	slug = models.CharField(max_length=250)
	def __str__(self):
		return self.name
class CtgTypeModel(models.Model):
	name_type = models.CharField(max_length=250)
	ctg=models.ForeignKey(CtgModel , on_delete=models.CASCADE)

	def __str__(self):
		return self.name_type
class ProductModel(models.Model):
	title= models.CharField(max_length=250)
	brand = models.CharField(max_length=250)
	image = models.ImageField()
	image1 = models.ImageField(null=True,blank=True)
	image2 = models.ImageField(null=True,blank=True)
	image3= models.ImageField(null=True,blank=True)
	text=models.TextField()
	price=models.IntegerField()
	is_active=models.BooleanField(default=True)
	ctgType=models.ForeignKey(CtgTypeModel ,  on_delete=models.CASCADE)
	
	def __str__(self):
		return self.title 
class  Karzinka(models.Model):
	title_k   = models.CharField(max_length=250)
	image_k   = models.ImageField()
	price_k   =models.IntegerField()
	date_k=models.DateTimeField(auto_now=True)
	is_delier=models.BooleanField(default=False)
	username  =models.CharField(max_length=250)
	catrgory_k=models.CharField(max_length=250)
	soni      =models.IntegerField(default=1)
	total_cost=models.IntegerField(null=True ,blank=True)
	def __str__(self):
		return self.title_k 		
class ClientModel(models.Model):
	user_client=models.CharField(max_length=250)
	phone=models.CharField(max_length=250)
	mobile=models.CharField(max_length=250)
	def __str__(self):
		return self.user_client