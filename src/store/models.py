from django.db import models

from app.choices import StatusChoices


class Warehouse(models.Model):
    # This model will be synchronized with warehouses in warehouse app
    name = models.CharField(max_length=256, verbose_name="Warehouse name")
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = "store_warehouse"


class StoreOrder(models.Model):
    number = models.CharField(max_length=256, verbose_name="Order number")
    status = models.CharField(
        max_length=25, choices=StatusChoices, default=StatusChoices.NEW
    )
    warehouse_order_id = models.IntegerField(
        verbose_name="Warehouse order ID", blank=True, null=True, default=None
    )
    warehouse = models.ForeignKey(
        Warehouse,
        on_delete=models.DO_NOTHING,
        related_name="orders",
        verbose_name="Warehouse",
    )

    class Meta:
        db_table = "store_order"
