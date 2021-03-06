# Generated by Django 4.0.3 on 2022-07-02 14:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('commons', '0006_alter_periodicity_period'),
        ('listings', '0012_allpurposepropertyunitlisting_all_purpose_property'),
    ]

    operations = [
        migrations.AddField(
            model_name='mainlisting',
            name='listing_term',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='commons.periodicity', verbose_name='listing term (i.e. per month, per year)'),
        ),
    ]
