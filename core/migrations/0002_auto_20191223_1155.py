# Generated by Django 2.2.7 on 2019-12-23 10:55

import ckeditor.fields
import core.helpers
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomePageSlider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('active', models.BooleanField(default=False)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Home Page Slider',
                'verbose_name_plural': 'Home Page Sliders',
                'ordering': ['-updated'],
            },
        ),
        migrations.CreateModel(
            name='MainPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('sub_title', models.CharField(blank=True, max_length=255, null=True)),
                ('img', models.ImageField(blank=True, help_text='Image size should be 922x731 px', null=True, upload_to='pages/img', verbose_name='Main Image')),
                ('body', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('vid_file', models.FileField(blank=True, help_text='Upload Video File', null=True, upload_to='blog/videos')),
                ('youtube_video_id', models.CharField(blank=True, help_text='Youtube Video ID e.g L0I7i_lE5zA. Not Complete Url', max_length=20, null=True)),
                ('extra_info', tinymce.models.HTMLField(blank=True, null=True)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('on_navigation', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Main Page',
                'verbose_name_plural': 'Main Pages',
                'ordering': ['-title'],
            },
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('sub_title', models.CharField(blank=True, max_length=100, null=True)),
                ('logo', models.ImageField(help_text='Image size is 340x145 px', upload_to='partners')),
                ('website', models.CharField(help_text='Start with http:// or https://', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='SiteInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('info', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Site Information',
                'verbose_name_plural': 'Site Informations',
                'ordering': ['-updated'],
            },
        ),
        migrations.RenameField(
            model_name='address',
            old_name='zip',
            new_name='zip_code',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='dob',
            field=models.DateField(blank=True, help_text='Date of Birth', null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')], default='Others', help_text='Gender', max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(blank=True, help_text='Image size is 270x308 px', null=True, upload_to='profile_pics'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='payant_customer_id',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='paystack_customer_id',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='phone_number',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='reg_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='state',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='uid',
            field=models.CharField(default=core.helpers.getUniqueId, editable=False, max_length=20),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='addresses', to='core.UserProfile'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='SliderImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.ImageField(help_text='Image size is 1900px width and 1267px height', upload_to='sliders/img')),
                ('header', models.CharField(max_length=100)),
                ('sub_title', models.CharField(blank=True, max_length=300, null=True)),
                ('button_1', models.CharField(blank=True, max_length=50, null=True)),
                ('button_1_url', models.CharField(blank=True, max_length=100, null=True)),
                ('button_2', models.CharField(blank=True, max_length=50, null=True)),
                ('button_2_url', models.CharField(blank=True, max_length=100, null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('slider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sliders', to='core.HomePageSlider')),
            ],
            options={
                'verbose_name': 'Slider Image',
                'verbose_name_plural': 'Slider Images',
                'ordering': ['-updated'],
            },
        ),
    ]