# Generated by Django 3.2.9 on 2022-01-14 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0009_auto_20211207_1243'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='mimage',
            field=models.ImageField(blank=True, null=True, upload_to='members/'),
        ),
    ]