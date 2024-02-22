from .models import *
from django.forms import ModelForm

class CategoryProductForm(ModelForm):
    class Meta:
        model = CategoryProductModel
        fields = '__all__'

class StoreProductForm(ModelForm):
    class Meta:
        model = StoreProductModel
        fields = '__all__'

class ProductPriceForm(ModelForm):
    class Meta:
        model = ProductPriceModel
        fields = '__all__'

class ProductForm(ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['category'].empty_label = 'Категория не выбрана'
        self.fields['store_product'].empty_label = 'Магазин не выбран'

    class Meta:
        model = ProductModel
        fields = ['name','description','developer','category','store_product']