# Generated by Django 2.1.2 on 2019-05-28 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0012_remove_plate_cost'),
    ]

    operations = [
        migrations.AddField(
            model_name='plate',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/plates/'),
        ),
    ]