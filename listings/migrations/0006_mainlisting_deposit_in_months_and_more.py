# Generated by Django 4.0.3 on 2022-06-16 22:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('systems', '0008_remove_listingparameter_value_and_more'),
        ('listings', '0005_alter_mainlisting_listing_mode_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='mainlisting',
            name='deposit_in_months',
            field=models.SmallIntegerField(default=0, verbose_name='number of months that deposit is required'),
        ),
        migrations.AddField(
            model_name='mainlisting',
            name='listing_currency',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='systems.currency', verbose_name='property price currency type'),
        ),
        migrations.AddField(
            model_name='mainlisting',
            name='property_price',
            field=models.FloatField(default=0.0, verbose_name='property price'),
        ),
    ]
