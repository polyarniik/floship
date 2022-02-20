from django.db import models

from app.choices import StatusChoices
from store.models import StoreOrder


class Warehouse(models.Model):
    name = models.CharField(max_length=256, verbose_name="Warehouse name")
    is_active = models.BooleanField(default=True, verbose_name="Is active")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "warehouse"


class WarehouseOrder(models.Model):
    number = models.CharField(max_length=256, verbose_name="Order number")
    status = models.CharField(
        max_length=25,
        choices=StatusChoices,
        default=StatusChoices.NEW,
        verbose_name="Status",
    )
    store_order_id = models.IntegerField(
        verbose_name="Store order ID", blank=True, null=True, default=None
    )
    warehouse = models.ForeignKey(
        Warehouse,
        on_delete=models.CASCADE,
        related_name="orders",
        verbose_name="Warehouse",
    )

    def __str__(self):
        return f"{self.number}|{StatusChoices.labels[self.status]}|{self.warehouse}"

    class Meta:
        db_table = "warehouse_order"
