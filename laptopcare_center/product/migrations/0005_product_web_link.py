# Generated by Django 4.2.11 on 2024-05-06 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_product_use_category_image_alter_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='web_link',
            field=models.URLField(blank=True, null=True),
        ),
    ]
