from django.shortcuts import render, redirect
from django.views.generic import FormView, ListView
from .forms import RegisterForm
from .models import Order
from user.models import User
from product.models import Product
from django.utils.decorators import method_decorator
from user.decorator import login_required
from django.db import transaction

# Create your views here.


@method_decorator(login_required, name='dispatch')
class OrderCreate(FormView):
    form_class = RegisterForm
    success_url = '/product/'

    def form_valid(self, form):

        with transaction.atomic():
            prod = Product.objects.get(pk=form.data.get('product'))
            order = Order(
                quantity=form.data.get('quantity'),
                product=prod,
                user=User.objects.get(email=self.request.session.get('user'))
            )
            order.save()
            prod.stock -= int(form.data.get('quantity'))
            prod.save()
        return super().form_valid(form)

    def form_invalid(self, form):

        return redirect('/product/' + str(form.product))

    # form을 생성할때 어떤 인자값을 전달해서 만들건지 결정
    def get_form_kwargs(self, **kwargs):
        kw = super().get_form_kwargs(**kwargs)
        kw.update({
            'request': self.request
        })
        return kw


@method_decorator(login_required, name='dispatch')
class OrderView(ListView):
    template_name = 'order.html'
    context_object_name = 'order_list'
    print("order인스턴스 생성됨.")

    def get_queryset(self, **kwargs):
        queryset = Order.objects.filter(
            user__email=self.request.session.get('user'))
        return queryset
