from rest_framework import serializers

from warehouse.models import WarehouseOrder, Warehouse


class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = "__all__"


class WarehouseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = WarehouseOrder
        fields = ("id", "number", "status", "store_order_id", "warehouse")
