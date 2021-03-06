# Generated by Django 4.0.3 on 2022-06-14 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('systems', '0004_rename_param_name_listingparameter_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='listingparameter',
            name='applied_to',
            field=models.CharField(choices=[('SUBSCRIPTION', 'Subscription'), ('PAY_PER_LISTING', 'Pay-per-listing'), ('BOTH', 'Subscription and Pay-per-listing')], default='SUBSCRIPTION', max_length=50, verbose_name='Which payment type to apply to'),
        ),
    ]
