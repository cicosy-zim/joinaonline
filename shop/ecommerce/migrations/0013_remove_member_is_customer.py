# Generated by Django 3.2.9 on 2022-02-11 11:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0012_merge_0010_member_mimage_0011_auto_20220129_1631'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='is_customer',
        ),
    ]
