from django.db import models


class WarehouseRouter:
    def db_for_read(self, model: models.Model, **hints):
        if model._meta.app_label == "warehouse":
            return "db_warehouse"
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == "warehouse":
            return "db_warehouse"
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == "warehouse":
            return db == "db_warehouse"
        return None
