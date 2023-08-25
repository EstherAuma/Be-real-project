from django.shortcuts import render

# Create your views here.


from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect

#here we are importing our models
from .models import *

#importing forms
from .forms import *

#importing filters
from .filters import *


#importing decorators
#login_required is to protect a view,can only be accessed after loging in.
from django.contrib.auth.decorators import login_required

#importing reverse
from django.urls import reverse

def index(request):
    return render(request,'dan/index.html')

def login(request):
    return render(request,'dan/login.html')


def home(request):
    
#we  are querrying our database
#asking the db to get all the products in models and order them by id.
    products = Product.objects.all().order_by('id')

#filter what you have already fetched/got
    product_filters = ProductFilter(request.GET,queryset = products)
    product = product_filters.qs
    

    #telling django to consider home.html
    #the home page will be displayed and where you are able to query the db/search
    return render(request,'dan/home.html',{'products':product,'product_filters':product_filters})


@login_required
def all_sales(request):
    sales = Sale.objects.all()
    total = sum([items.amount_recieved for items in sales])
    change = sum([items.get_change() for items in sales])
    net = total - change
    return render(request,'dan/all_sales.html',{'sales':sales,'change':change,'total':total,'net':net,})


@login_required
def product_detail(request,product_id):
    product = Product.objects.get(id=product_id)
    return render(request,'dan/product_detail.html',{'product': product})
    



@login_required
def receipt(request):
    sales = Sale.objects.all().order_by('-id')
    return render(request,'dan/receipt.html',{'sales':sales})
    


def receipt_detail(request,receipt_id):
    receipt = Sale.objects.get(id = receipt_id)
    return render(request,'dan/receipt_detail.html',{'receipt':receipt}) 
  



@login_required
def delete_detail(request, product_id):
    delete_product =Product.objects.get(id=product_id)
    delete_product.delete()
    return HttpResponseRedirect(reverse('home')) 

def register(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request,'dan/register.html',{'form':form})
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            return redirect('login')
        else:
            return render(request,'dan/register.html',{'form':form})



@login_required
def add_to_stock(request,pk):
    issued_item = Product.objects.get(id=pk)
    form = AddForm(request.POST)

    if request.method == 'POST':

        if form.is_valid():
            added_quantity=int(request.POST['recieved_quantity'])
            issued_item.total_quantity += added_quantity
            issued_item.save()
            #to add to the remaining stock, quantity is reduced.
            print(added_quantity)
            print(issued_item.total_quantity)
            #you are redirected to the home page after when you are done with the form
            return redirect('home')
    return render(request,'dan/add_to_stock.html',{'form':form})


@login_required
def issue_item(request,pk):
    issued_item = Product.objects.get(id = pk)
    sales_form = SaleForm(request.POST)

    if request.method == 'POST':
        if sales_form.is_valid():
            new_sale = sales_form.save(commit = False)
            new_sale.item = issued_item
            new_sale.unit_price = issued_item.unit_price
            new_sale.save()
            #keep track of items remaining  after sale
            issued_quantity = int(request.POST['quantity'])
            issued_item.total_quantity -=  issued_quantity
            issued_item.save()

            print(issued_item.item_name)

            print(request.POST['quantity'])
            print(issued_item.total_quantity)
            return redirect('receipt')
    return render(request,'dan/issue_item.html',{'sales_form':sales_form})



