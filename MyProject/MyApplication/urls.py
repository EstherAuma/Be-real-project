from django.urls import path
from MyApplication import views
#let's reuse the django login view
from django.contrib.auth import views as auth_views
#auth_views can be any name and will be the name of views
urlpatterns = [
   
   path('',views.index,name='index'),
   
   path('home',views.home,name='home'),

   path('login/',auth_views.LoginView.as_view(template_name ='dan/login.html'), name = 'login'),
   
   path('home/<int:product_id>',views.product_detail,name='product_detail'),
   
   path('receipt/',views.receipt, name = 'receipt'),

   path('receipt_detail/<int:receipt_id>',views.receipt_detail, name = 'receipt_detail'),

   
   path('issue_item/<str:pk>',views.issue_item, name = 'issue_item'),

   path('all_sales/',views.all_sales, name = 'all_sales'),


   path('add_to_stock/<int:pk>',views.add_to_stock, name ='add_to_stock'),

   path('login/',auth_views.LogoutView.as_view(template_name ='dan/logout.html'), name = 'logout'),
   
   path('delete/<int:product_id>',views.delete_detail, name= 'delete_detail'),

   path('register/', views.register, name='register'),
   
]



