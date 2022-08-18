
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path('', views.ProductDetailsAPIView.as_view()),
    path('<int:pk>/', views.product_details_view, name='product-details'),
    path('<int:pk>/update/', views.product_update_view, name='product-edit'),
    path('<int:pk>/delete/', views.product_delete_view),

    path('', views.product_list_create_view),
    # path('<int:pk>/', views.product_alt_view),
    # path('', views.product_alt_view),


]
