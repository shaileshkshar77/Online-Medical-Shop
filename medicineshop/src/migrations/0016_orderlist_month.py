# Generated by Django 3.0.5 on 2021-02-05 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0015_auto_20210203_1713'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderlist',
            name='month',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
