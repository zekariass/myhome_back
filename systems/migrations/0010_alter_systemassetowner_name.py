# Generated by Django 4.0.3 on 2022-07-31 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('systems', '0009_rename_asset_path_systemasset_asset_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='systemassetowner',
            name='name',
            field=models.CharField(max_length=250, unique=True, verbose_name='name of owner of asset, (i.e. page)'),
        ),
    ]
