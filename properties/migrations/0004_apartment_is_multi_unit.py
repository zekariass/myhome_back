# Generated by Django 4.0.3 on 2022-05-04 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0003_hall'),
    ]

    operations = [
        migrations.AddField(
            model_name='apartment',
            name='is_multi_unit',
            field=models.BooleanField(blank=True, default=False, verbose_name='is multi unit?'),
        ),
    ]
