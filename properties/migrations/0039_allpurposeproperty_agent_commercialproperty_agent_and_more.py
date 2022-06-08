# Generated by Django 4.0.3 on 2022-06-07 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0038_villa_agent_alter_allpurposeproperty_property_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='allpurposeproperty',
            name='agent',
            field=models.BigIntegerField(blank=True, null=True, verbose_name='agent who creates the all purpose property'),
        ),
        migrations.AddField(
            model_name='commercialproperty',
            name='agent',
            field=models.BigIntegerField(blank=True, null=True, verbose_name='agent who creates the commercial property'),
        ),
        migrations.AddField(
            model_name='condominium',
            name='agent',
            field=models.BigIntegerField(blank=True, null=True, verbose_name='agent who creates the condominium'),
        ),
        migrations.AddField(
            model_name='hall',
            name='agent',
            field=models.BigIntegerField(blank=True, null=True, verbose_name='agent who creates the hall'),
        ),
        migrations.AddField(
            model_name='land',
            name='agent',
            field=models.BigIntegerField(blank=True, null=True, verbose_name='agent who creates the land'),
        ),
        migrations.AddField(
            model_name='office',
            name='agent',
            field=models.BigIntegerField(blank=True, null=True, verbose_name='agent who creates the office'),
        ),
        migrations.AddField(
            model_name='sharehouse',
            name='agent',
            field=models.BigIntegerField(blank=True, null=True, verbose_name='agent who creates the sharehouse'),
        ),
        migrations.AddField(
            model_name='traditionalhouse',
            name='agent',
            field=models.BigIntegerField(blank=True, null=True, verbose_name='agent who creates the traditionalhouse'),
        ),
    ]
