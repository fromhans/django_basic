from enum import auto
from django.db import models

# Create your models here.


class Order(models.Model):
    # ForeignKey 삭제시 반드시 on delete를 추가해줘야한다.
    # 해당 코드 추가시, 사용자가 삭제되면 주문도 같이 삭제된다.
    user = models.ForeignKey(
        'user.User', on_delete=models.CASCADE, verbose_name='사용자')
    product = models.ForeignKey(
        'product.Product', on_delete=models.CASCADE, verbose_name='상품')
    quantity = models.IntegerField(verbose_name='수량')
    register_date = models.DateTimeField(
        auto_now_add=True, verbose_name="등록날짜")

    def __str__(self):
        return str(self.user) + ' ' + str(self.product) + ' ' + str(self.quantity)

    class Meta:
        db_table = 'basic_order'
        verbose_name = '주문'
        verbose_name_plural = '주문 복수'
