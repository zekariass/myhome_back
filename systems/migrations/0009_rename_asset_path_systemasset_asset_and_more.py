# Generated by Django 4.0.3 on 2022-07-31 16:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('systems', '0008_remove_listingparameter_value_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='systemasset',
            old_name='asset_path',
            new_name='asset',
        ),
        migrations.RenameField(
            model_name='systemasset',
            old_name='asset_description',
            new_name='description',
        ),
        migrations.RemoveField(
            model_name='systemasset',
            name='asset_type',
        ),
        migrations.RemoveField(
            model_name='systemassetowner',
            name='asset',
        ),
        migrations.RemoveField(
            model_name='systemassetowner',
            name='owner',
        ),
        migrations.AddField(
            model_name='systemasset',
            name='name',
            field=models.CharField(default=None, max_length=50, unique=True, verbose_name='system asset name'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='systemasset',
            name='owner',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='assets', to='systems.systemassetowner'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='systemassetowner',
            name='name',
            field=models.CharField(default='', max_length=250, unique=True, verbose_name='Name of owner of Asset, (i.e. Page)'),
            preserve_default=False,
        ),
    ]
