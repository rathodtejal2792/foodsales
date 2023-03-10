# Generated by Django 4.1.1 on 2023-01-23 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FoodTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('OrderDate', models.DateField()),
                ('Region', models.CharField(max_length=200)),
                ('City', models.CharField(max_length=200)),
                ('Category', models.CharField(max_length=200)),
                ('Product', models.CharField(max_length=200)),
                ('Quantity', models.IntegerField(default=0)),
                ('UnitPrice', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
            ],
        ),
    ]
