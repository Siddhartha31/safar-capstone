# Generated by Django 3.1.7 on 2021-04-21 19:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fund', '0002_auto_20210407_2244'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accept',
            name='account_id',
        ),
        migrations.AlterField(
            model_name='accept',
            name='request_id',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='fund.request'),
        ),
        migrations.AlterField(
            model_name='request',
            name='request_category',
            field=models.CharField(choices=[('MEDICAL', 'MEDICAL'), ('LITERACY AND EDUCATION', 'LITERACY AND EDUCATION'), ('HUMAN RIGHTS', 'HUMAN RIGHTS'), ('PHYSICAL HELP', 'PHYSICAL HELP'), ('POVERTY', 'POVERTY'), ('OTHER', 'OTHER')], default='OTHER', max_length=50),
        ),
    ]
