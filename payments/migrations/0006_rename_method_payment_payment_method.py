# Generated by Django 4.0.3 on 2022-06-12 09:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0005_rename_paid_on_bankpayment_payment_date_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='method',
            new_name='payment_method',
        ),
    ]
