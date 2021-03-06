from django.shortcuts import render
from django.views.generic import ListView, FormView, DetailView

from product.serializers import ProductSerializer
from .models import Product
from .forms import RegisterForm
from order.forms import RegisterForm as OrderForm
from user.decorator import login_required, admin_required
from django.utils.decorators import method_decorator
from rest_framework import generics, mixins
from rest_framework.response import Response
# Create your views here.


# serializer를 활용
# 데이터 검증 -> 시리얼라이저,
# 어떤 데이터를 가져올지 -> get_queryset 상속 후 재구현
class ProductListAPI(generics.GenericAPIView, mixins.ListModelMixin):
    # 시리얼라이저와 쿼리셋을 지정
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.all().order_by('id')

    def get(self, request, *args, **kwargs):

        # list함수는 모델로부터 리스트를 받아오고 json 형식으로 변환해준다.
        return self.list(request, *args, **kwargs)


class ProductDetailAPI(generics.GenericAPIView, mixins.RetrieveModelMixin):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.all().order_by('id')

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class ProductView(ListView):
    model = Product
    template_name = 'product.html'
    context_object_name = 'product_list'
    print("product인스턴스 생성됨.")
    print(model)


@method_decorator(admin_required, name='dispatch')
class ProductCreate(FormView):
    template_name = 'register_product.html'
    form_class = RegisterForm
    success_url = '/product/'

    def form_valid(self, form):
        product = Product(
            name=form.data.get('name'),
            price=form.data.get('price'),
            description=form.data.get('description'),
            stock=form.data.get('stock')
        )
        product.save()
        return super().form_valid(form)


class ProductDetail(DetailView):
    model = Product
    template_name = 'product_detail.html'
    queryset = Product.objects.all()
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = OrderForm(self.request)
        return context
