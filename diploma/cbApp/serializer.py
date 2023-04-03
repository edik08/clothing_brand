from rest_framework import serializers
import cbApp.models as cb_models


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = cb_models.Products
        fields = ('id',
                  'title',
                  'cost',
                  'id_material')
