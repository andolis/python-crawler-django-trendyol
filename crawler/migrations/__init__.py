from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='crawlerTrendyol',
            fields=[
                ('tid', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tUrl', models.CharField(default=False, max_length=255)),
                ('tName', models.CharField(default='', max_length=40)),
                ('tBrand', models.CharField(default='', max_length=40)),
                ('tPriceSell', models.CharField(default='', max_length=40)),
                ('tPriceDiscount', models.CharField(default='', max_length=40)),
                ('tCategory', models.CharField(default='', max_length=255)),
                ('tMerchantName', models.CharField(default='', max_length=255)),
                ('tMerchantCity', models.CharField(default='', max_length=40)),
                ('tMerchantSellerScore', models.CharField(default='', max_length=40)),
                ('tOtherMerchant', models.CharField(default='', max_length=255)),
            ],
        ),
    ]