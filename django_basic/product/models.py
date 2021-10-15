from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=256, verbose_name='상품명')
    price = models.IntegerField(verbose_name="가격")
    description = models.TextField(verbose_name='상품설명')
    # 텍스트필드와 캐릭터필드의 가장 큰 차이점은 길이 제한.
    stock = models.IntegerField(verbose_name='재고')
    register_date = models.DateTimeField(
        auto_now_add=True, verbose_name='등록날짜')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'basic_product'
        verbose_name = '상품'
        verbose_name_plural = '상품 복수'
