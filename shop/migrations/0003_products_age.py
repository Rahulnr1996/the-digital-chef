# Generated by Django 2.2 on 2022-04-28 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_products'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='age',
            field=models.IntegerField(default=1232),
            preserve_default=False,
        ),
    ]
