# Generated by Django 2.2.7 on 2019-12-26 16:28

import core.helpers
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_auto_20191225_1637'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='trans',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='trxref',
        ),
        migrations.AddField(
            model_name='payment',
            name='complete',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='fashioninsta',
            name='ankle',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Base/Ankle'),
        ),
        migrations.AlterField(
            model_name='fashioninsta',
            name='biceps',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Biceps'),
        ),
        migrations.AlterField(
            model_name='fashioninsta',
            name='calf',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Calf'),
        ),
        migrations.AlterField(
            model_name='fashioninsta',
            name='chest',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Chest'),
        ),
        migrations.AlterField(
            model_name='fashioninsta',
            name='hip',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Sit/Hip'),
        ),
        migrations.AlterField(
            model_name='fashioninsta',
            name='knee',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Knee'),
        ),
        migrations.AlterField(
            model_name='fashioninsta',
            name='laps',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Laps'),
        ),
        migrations.AlterField(
            model_name='fashioninsta',
            name='neck',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Neck'),
        ),
        migrations.AlterField(
            model_name='fashioninsta',
            name='round_sleeve',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Round Sleeve'),
        ),
        migrations.AlterField(
            model_name='fashioninsta',
            name='shirt',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Shirt Length'),
        ),
        migrations.AlterField(
            model_name='fashioninsta',
            name='shoulder',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Shoulder'),
        ),
        migrations.AlterField(
            model_name='fashioninsta',
            name='sleeve',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Sleeve Length'),
        ),
        migrations.AlterField(
            model_name='fashioninsta',
            name='slug',
            field=models.CharField(blank=True, default=core.helpers.getUniqueId, editable=False, help_text="<b style='color:red'>Do Not Edit</b>", max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='fashioninsta',
            name='tommy',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Tommy'),
        ),
        migrations.AlterField(
            model_name='fashioninsta',
            name='trouser_lenght',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Trouser Lenght'),
        ),
        migrations.AlterField(
            model_name='fashioninsta',
            name='trouser_waist',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Trouser Waist'),
        ),
        migrations.AlterField(
            model_name='fashioninsta',
            name='wrist',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Cuff/Wrist'),
        ),
        migrations.AlterField(
            model_name='item',
            name='inventory',
            field=models.PositiveIntegerField(blank=True, help_text='How many of the Product are available', null=True),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
        ),
    ]