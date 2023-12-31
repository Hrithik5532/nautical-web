# Generated by Django 4.2.4 on 2023-10-11 07:35

import Home.models
import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0014_applicationsforjob'),
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(default=Home.models.generate_uid, editable=False, max_length=6)),
                ('img', models.FileField(upload_to='services/')),
                ('headline', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('content', ckeditor.fields.RichTextField(blank=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='applicationsforjob',
            name='JobPosition',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='Home.jobpositions'),
        ),
        migrations.AlterField(
            model_name='applicationsforjob',
            name='contact',
            field=models.CharField(editable=False, max_length=15),
        ),
        migrations.AlterField(
            model_name='applicationsforjob',
            name='email',
            field=models.EmailField(editable=False, max_length=254),
        ),
        migrations.AlterField(
            model_name='applicationsforjob',
            name='expected_ctc',
            field=models.CharField(editable=False, max_length=40),
        ),
        migrations.AlterField(
            model_name='applicationsforjob',
            name='experiance',
            field=models.CharField(editable=False, max_length=50),
        ),
        migrations.AlterField(
            model_name='applicationsforjob',
            name='name',
            field=models.CharField(editable=False, max_length=100),
        ),
        migrations.AlterField(
            model_name='applicationsforjob',
            name='resume',
            field=models.FileField(editable=False, upload_to='Job-applicants/'),
        ),
    ]
