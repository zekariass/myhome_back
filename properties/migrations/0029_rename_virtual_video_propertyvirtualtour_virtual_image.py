# Generated by Django 4.0.3 on 2022-05-29 09:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0028_alter_propertyimage_property_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='propertyvirtualtour',
            old_name='virtual_video',
            new_name='virtual_image',
        ),
    ]
