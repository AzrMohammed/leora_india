# Generated by Django 2.2.6 on 2020-11-28 15:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('GEN', '0019_auto_20201128_2119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='brandbranch',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='GEN.BrandBranchBasicInfo'),
        ),
    ]
