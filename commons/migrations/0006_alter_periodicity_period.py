# Generated by Django 4.0.3 on 2022-07-02 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commons', '0005_remove_periodicity_period_periodicity_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='periodicity',
            name='period',
            field=models.CharField(max_length=30, unique=True, verbose_name='period label or name'),
        ),
    ]