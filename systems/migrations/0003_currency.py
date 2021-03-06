# Generated by Django 4.0.3 on 2022-06-11 22:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('systems', '0002_listingparameter_param_value_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Birr', max_length=20, verbose_name='Currency name')),
                ('numeric_code', models.CharField(default=230, max_length=5, verbose_name='Numeric code of the currency')),
                ('symbol', models.CharField(default='Br', max_length=10, verbose_name='Symbol of the currency')),
                ('added_on', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
            ],
        ),
    ]
