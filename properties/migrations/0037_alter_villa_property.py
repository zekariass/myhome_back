# Generated by Django 4.0.3 on 2022-06-04 21:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0036_apartment_agent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='villa',
            name='property',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='villa', to='properties.property', verbose_name='parent property'),
        ),
    ]