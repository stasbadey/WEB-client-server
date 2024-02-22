from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('store_print/', views.store_print, name='store_print'),
    path('category_print/', views.category_print, name='category_print'),
    path('price_print/', views.price_print, name='price_print'),
    path('product_print/', views.product_print, name='product_print'),
    path('create_store/', views.create_store, name='create_store'),
    path('create_category/', views.create_category, name='create_category'),
    path('create_price/', views.create_price, name='create_price'),
    path('create_product/', views.create_product, name='create_product'),
    path('<int:id>/edit_store', views.edit_store, name='edit_store'),
    path('<int:id>/edit_categories', views.edit_category, name='edit_category'),
    path('<int:id>/edit_price', views.edit_price, name='edit_price'),
    path('<int:id>/edit_product', views.edit_product, name='edit_product'),
    path('store/delete/<int:id>/', views.delete_store, name='delete_store'),
    path('price/delete/<int:id>/', views.delete_price, name='delete_price'),
    path('category/delete/<int:id>/', views.delete_category, name='delete_category'),
    path('product/delete/<int:id>/', views.delete_product, name='delete_product'),
    # path('create_product/',views.AddProduct.as_view(),name='create_product'),
]
