from django.db import models


class StoreRouter:
    def db_for_read(self, model: models.Model, **hints):
        if model._meta.app_label == "store":
            return "db_store"
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == "store":
            return "db_store"
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == "store":
            return db == "db_store"
        return None
