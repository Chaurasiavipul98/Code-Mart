# Generated by Django 5.1.5 on 2025-04-05 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_alter_developerprofile_bio'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerprofile',
            name='has_subscription',
            field=models.BooleanField(default=False),
        ),
    ]
