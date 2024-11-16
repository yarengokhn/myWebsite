from product.models import Product
from rest_framework import serializers

#Serializer'lar, Django modellerinden veya veritabanı nesnelerinden gelen verileri JSON gibi formatlara dönüştürmek için kullanılır, aynı zamanda kullanıcıdan gelen verileri doğrulamak ve işlemek için de kullanılır.
# class ProductSerializer(serializers.Serializer):
#     id=serializers.IntegerField(read_only=True)
#     title = serializers.CharField()
#     price = serializers.IntegerField(read_only=True)
#     quantity = serializers.IntegerField(read_only=True)
#     description = serializers.CharField()
#     product_category = serializers.CharField()


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields= '__all__'
        # fields = ('id','title')


    def create(self, validated_data):
        return Product.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.product_category = validated_data.get('product_category', instance.product_category)
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.keywords = validated_data.get('keywords', instance.keywords)
        instance.price = validated_data.get('price', instance.price)
        instance.amount = validated_data.get('amount', instance.amount)
        instance.detail = validated_data.get('detail', instance.detail)
        instance.save()
        return instance