# Generated by Django 3.2.9 on 2021-12-06 13:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0004_auto_20211201_1634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='ecommerce.category'),
        ),
        migrations.CreateModel(
            name='Sub_Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=250, unique=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sub_categories', to='ecommerce.category')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='sub_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='ecommerce.sub_category'),
        ),
    ]
