from django.contrib import admin, messages
from .models import crawlerTrendyol
from .services import TrendyolServiceCrawler

class TrendyolAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Url", {"fields": ["tUrl"]}),
        ("Detail", {"fields": [
            "tName",
            "tBrand",
            "tPriceSell",
            "tPriceDiscount",
            "tCategory",
            "tMerchantName",
            "tMerchantCity",
            "tMerchantSellerScore"
        ]}),
    ]

    def save_model(self, request, obj, form, change):
        if request.method == "POST":
            tUrl = request.POST.get('tUrl')
            newCrawler = TrendyolServiceCrawler()
            newCrawler.setCrawlerUrl(tUrl)
            crawlerDetail = newCrawler.getDetail()
            if crawlerDetail is False:
                messages.error(request, "Url Detail Not Found")
            else:
                obj.tUrl = crawlerDetail["tUrl"]
                obj.tName = crawlerDetail["tName"]
                obj.tBrand = crawlerDetail["tBrand"]
                obj.tPriceSell = crawlerDetail["tPriceSell"]
                obj.tPriceDiscount = crawlerDetail["tPriceDiscount"]
                obj.tCategory = crawlerDetail["tCategory"]
                obj.tMerchantName = crawlerDetail["tMerchantName"]
                obj.tMerchantCity = crawlerDetail["tMerchantCity"]
                obj.tMerchantSellerScore = crawlerDetail["tMerchantSellerScore"]
                obj.tOtherMerchant = crawlerDetail["tOtherMerchant"]
                super().save_model(request, obj, form, change)



# Register your models here.
admin.site.register(crawlerTrendyol, TrendyolAdmin)
