from django.db import models


class AllProducts(models.Model):
    uniq_id = models.CharField(max_length=255, primary_key=True)
    crawl_timestamp = models.DateTimeField(null=True)
    product_url = models.URLField(max_length=1000, null=True)
    product_name = models.CharField(max_length=1000, null=True)
    product_category_tree = models.JSONField(null=True)
    pid = models.CharField(max_length=100, null=True)
    retail_price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    discounted_price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    image = models.JSONField(null=True)
    is_FK_Advantage_product = models.BooleanField(null=True)
    description = models.TextField(max_length=5000, null=True)
    product_rating = models.IntegerField(null=True)
    overall_rating = models.IntegerField(null=True)
    brand = models.CharField(max_length=255, null=True)
    product_specifications = models.JSONField(null=True)


class RelaxedFit(models.Model):
    fabric = models.CharField(max_length=100, default="")
    ideal_for = models.CharField(max_length=100, default="")


class RegularFit(models.Model):
    fabric = models.CharField(max_length=100, default="")
    ideal_for = models.CharField(max_length=100, default="")
