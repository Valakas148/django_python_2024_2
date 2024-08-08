from django.db import models


class QuerySetManager(models.QuerySet):
    def less_than_price(self, price):
        return self.filter(pk__lt=price)

    def only_brand(self, brand):
        return self.filter(brand=brand)

class CarManager(models.Manager):
    def get_queryset(self):
        return QuerySetManager(self.model)

    def less_than_price(self, price):
        return self.get_queryset().less_than_price(price)

    def only_brand(self, brand):
        return self.get_queryset().only_brand(brand)