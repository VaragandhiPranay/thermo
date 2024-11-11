# Generated by Django 5.1.3 on 2024-11-11 16:54

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('user_id', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('group', models.CharField(choices=[('development', 'Development'), ('commercial', 'Commercial'), ('production', 'Production'), ('service', 'Service'), ('users', 'Users'), ('other', 'Other')], max_length=20)),
                ('role', models.CharField(choices=[('viewer', 'Viewer'), ('designer', 'Designer'), ('other', 'Other')], max_length=20)),
                ('employment_type', models.CharField(choices=[('MSD', 'MSD'), ('other', 'Other')], max_length=20)),
                ('company_name', models.CharField(blank=True, max_length=50, null=True)),
                ('ip_clearance_level', models.IntegerField(blank=True, choices=[(1, 'Level 1'), (3, 'Level 3')], null=True)),
                ('license_level', models.CharField(default='Consumer', max_length=20)),
                ('ip_clearance_status', models.CharField(blank=True, max_length=20, null=True)),
                ('catalog_tasks_id', models.CharField(blank=True, max_length=50, null=True)),
                ('submission_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.DeleteModel(
            name='UserAccount',
        ),
    ]