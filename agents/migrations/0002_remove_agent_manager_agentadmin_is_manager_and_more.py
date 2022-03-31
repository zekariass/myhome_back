# Generated by Django 4.0.3 on 2022-03-31 22:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('agents', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agent',
            name='manager',
        ),
        migrations.AddField(
            model_name='agentadmin',
            name='is_manager',
            field=models.BooleanField(default=False, verbose_name='is admin the main manager?'),
        ),
        migrations.AlterField(
            model_name='agentadmin',
            name='admin',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender_party', models.CharField(choices=[('USER', 'User'), ('AGENT', 'Agent')], max_length=50, verbose_name='Who send the message?')),
                ('message', models.TextField()),
                ('sent_on', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('read', models.BooleanField(default=False, verbose_name='Does the receiver read the message?')),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='received_messages', to='agents.agent')),
                ('initiator_uer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_messages', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
