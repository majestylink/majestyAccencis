# Generated by Django 2.2.7 on 2019-12-23 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20191223_1507'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='label_type',
            field=models.CharField(choices=[('P', 'primary'), ('S', 'secondary'), ('D', 'danger')], default='P', max_length=1, verbose_name='Product Label Type'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='item',
            name='label',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Product Label'),
        ),
    ]
