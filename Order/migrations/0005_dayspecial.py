# Generated by Django 2.1.2 on 2019-05-26 12:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0004_plate_cost'),
    ]

    operations = [
        migrations.CreateModel(
            name='DaySpecial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('plate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Order.Plate')),
            ],
            options={
                'ordering': ('date',),
            },
        ),
    ]
