# Generated by Django 5.1.6 on 2025-03-07 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a_chat', '0005_alter_message_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='userchatstatus',
            name='last_deleted_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
