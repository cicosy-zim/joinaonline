# Generated by Django 3.2.9 on 2021-12-06 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0006_auto_20211206_1517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_slug',
            field=models.SlugField(blank=True, max_length=200, null=True),
        ),
    ]
