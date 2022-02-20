import requests
from django.contrib import admin, messages
from rest_framework.reverse import reverse

from store.serializers import (
    WarehouseSerializer as StoreWarehouseSerializer,
    StoreOrderSerializer,
)
from warehouse.models import Warehouse, WarehouseOrder


class WarehouseModelAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "is_active")
    list_editable = ("is_active",)
    search_fields = ("name",)
    list_filter = ("is_active",)

    def save_model(self, request, obj, form, change):
        data = StoreWarehouseSerializer(obj).data
        if change:
            response = requests.put(
                request.environ["HTTP_ORIGIN"]
                + reverse("store_warehouse-detail", kwargs={"pk": obj.id}),
                data=data,
            )
        else:
            response = requests.post(
                request.environ["HTTP_ORIGIN"] + reverse("store_warehouse-list"),
                data=data,
            )
        if str(response.status_code).startswith("2"):
            obj.save()
        else:
            messages.error(request, "Error when creating Warehouse")


class WarehouseOrderModelAdmin(admin.ModelAdmin):
    list_display = ("id", "number", "status", "store_order_id", "status")
    list_filter = ("status",)
    readonly_fields = ("store_order_id",)

    def save_model(self, request, obj, form, change):
        obj.save()
        data = StoreOrderSerializer(
            {
                "number": obj.number,
                "status": obj.status,
                "warehouse": obj.warehouse,
                "warehouse_order_id": obj.id,
            }
        ).data
        if change:
            response = requests.put(
                request.environ["HTTP_ORIGIN"]
                + reverse("store_order-detail", kwargs={"pk": obj.store_order_id}),
                data=data,
            )
        else:
            response = requests.post(
                request.environ["HTTP_ORIGIN"] + reverse("store_order-list"),
                data=data,
            )
        if str(response.status_code).startswith("2"):
            obj.store_order_id = int(response.json()["id"])
            obj.save()
        else:
            messages.error(request, "Error when creating Warehouse")


admin.site.register(Warehouse, WarehouseModelAdmin)
admin.site.register(WarehouseOrder, WarehouseOrderModelAdmin)
