# Generated by Django 4.0.3 on 2022-05-27 11:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0022_propertyvideo_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='property',
            old_name='Point_of_interest',
            new_name='point_of_interest',
        ),
        migrations.RenameField(
            model_name='property',
            old_name='TransportFacility',
            new_name='transport_facility',
        ),
    ]
