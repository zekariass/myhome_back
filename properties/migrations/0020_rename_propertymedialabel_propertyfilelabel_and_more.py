# Generated by Django 4.0.3 on 2022-05-18 17:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0019_allpurposeproperty_floors'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PropertyMediaLabel',
            new_name='PropertyFileLabel',
        ),
        migrations.AddField(
            model_name='propertyvideo',
            name='label',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='videos', to='properties.propertyfilelabel'),
        ),
        migrations.AddField(
            model_name='propertyvirtualtour',
            name='label',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='virtual_images', to='properties.propertyfilelabel'),
        ),
    ]
