import requests
from django.contrib import admin, messages
from rest_framework.reverse import reverse

from store.models import Warehouse, StoreOrder
from warehouse.serializers import WarehouseOrderSerializer


class WarehouseModelAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "is_active")
    list_editable = ("is_active",)

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class StoreOrderModelAdmin(admin.ModelAdmin):
    list_display = ("id", "number", "status", "warehouse_order_id", "warehouse")
    list_filter = ("status", "warehouse")
    readonly_fields = ("warehouse_order_id",)

    def save_model(self, request, obj: StoreOrder, form, change):
        obj.save()
        data = WarehouseOrderSerializer(
            {
                "number": obj.number,
                "status": obj.status,
                "warehouse": obj.warehouse,
                "store_order_id": obj.id,
            }
        ).data
        if change:
            response = requests.put(
                request.environ["HTTP_ORIGIN"]
                + reverse(
                    "warehouse_order-detail", kwargs={"pk": obj.warehouse_order_id}
                ),
                data=data,
            )
        else:
            response = requests.post(
                request.environ["HTTP_ORIGIN"] + reverse("warehouse_order-list"),
                data=data,
            )
        if str(response.status_code).startswith("2"):
            obj.warehouse_order_id = int(response.json()["id"])
            obj.save()
        else:
            messages.error(request, "Error when creating Warehouse")


admin.site.register(Warehouse, WarehouseModelAdmin)
admin.site.register(StoreOrder, StoreOrderModelAdmin)
