# Generated by Django 2.1.2 on 2019-05-26 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0003_menu_plates'),
    ]

    operations = [
        migrations.AddField(
            model_name='plate',
            name='cost',
            field=models.FloatField(default=0.0),
            preserve_default=False,
        ),
    ]
