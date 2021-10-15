from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    # 모델 연결을 위한 Meta class 선언
    class Meta:
        model = Product
        fields = '__all__'
        # fields 명시 안할경우 모델 안의 모든 필드를 가져옴.
