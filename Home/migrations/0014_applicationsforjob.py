# Generated by Django 4.2.4 on 2023-10-10 17:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0013_jobpositions_uid'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicationsForJob',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('contact', models.CharField(max_length=15)),
                ('experiance', models.CharField(max_length=50)),
                ('expected_ctc', models.CharField(max_length=40)),
                ('resume', models.FileField(upload_to='Job-applicants/')),
                ('JobPosition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Home.jobpositions')),
            ],
        ),
    ]
