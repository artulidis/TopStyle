# Generated by Django 3.2.6 on 2022-03-13 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0006_product_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='recommended',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]