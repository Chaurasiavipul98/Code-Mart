# Generated by Django 5.1.5 on 2025-04-10 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0008_modificationrequest_dispute_reason_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chatmessage',
            name='visibility',
        ),
        migrations.AlterField(
            model_name='modificationrequest',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('negotiating', 'Negotiating'), ('price_confirmed', 'Price Confirmed'), ('advance_paid', 'Advance Paid'), ('code_delivered', 'Code Delivered'), ('completed', 'Completed'), ('disputed', 'Disputed'), ('declined', 'Declined'), ('refunded', 'Refunded'), ('closed', 'Closed')], default='pending', max_length=20),
        ),
    ]
