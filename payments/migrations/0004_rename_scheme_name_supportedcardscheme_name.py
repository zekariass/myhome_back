# Generated by Django 4.0.3 on 2022-06-11 09:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0003_rename_parent_payment_bankpayment_payment_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='supportedcardscheme',
            old_name='scheme_name',
            new_name='name',
        ),
    ]
