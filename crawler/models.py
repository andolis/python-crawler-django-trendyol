from django.db import models


class crawlerTrendyol(models.Model):
    tId = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    tUrl = models.CharField(max_length=255, blank=False, default='')
    tName = models.CharField(max_length=40, blank=True, default='')
    tBrand = models.CharField(max_length=40, blank=True, default='')
    tPriceSell = models.CharField(max_length=40, blank=True, default='')
    tPriceDiscount = models.CharField(max_length=40, blank=True, default='')
    tCategory = models.CharField(max_length=255, blank=True, default='')
    tMerchantName = models.CharField(max_length=255, blank=True, default='')
    tMerchantCity = models.CharField(max_length=40, blank=True, default='')
    tMerchantSellerScore = models.CharField(max_length=40, blank=True, default='')
    tOtherMerchant = models.CharField(max_length=255, blank=True, default='')