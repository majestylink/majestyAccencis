# Generated by Django 2.2.7 on 2019-12-31 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0012_remove_payment_complete'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='allow_request',
            field=models.BooleanField(default=True, help_text='If the Product is available for fashion Requests'),
        ),
    ]
