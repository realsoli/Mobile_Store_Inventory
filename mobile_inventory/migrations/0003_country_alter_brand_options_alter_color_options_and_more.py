# Generated by Django 5.1.1 on 2024-09-26 07:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobile_inventory', '0002_phone_country_of_manufacture_alter_brand_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='نام کشور')),
            ],
            options={
                'verbose_name': 'کشور',
                'verbose_name_plural': 'کشورها',
            },
        ),
        migrations.AlterModelOptions(
            name='brand',
            options={'verbose_name': 'برند', 'verbose_name_plural': ' برند ها'},
        ),
        migrations.AlterModelOptions(
            name='color',
            options={'verbose_name': 'رنگ', 'verbose_name_plural': 'رنگ ها'},
        ),
        migrations.AlterModelOptions(
            name='phone',
            options={'verbose_name': 'موبایل', 'verbose_name_plural': 'موبایل ها'},
        ),
        migrations.AlterField(
            model_name='phone',
            name='country_of_manufacture',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='mobile_inventory.country', verbose_name='کشور سازنده'),
        ),
    ]