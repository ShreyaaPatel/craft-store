# Generated by Django 5.0 on 2023-12-26 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crafty', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='id',
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=200, primary_key=True, serialize=False),
        ),
    ]
