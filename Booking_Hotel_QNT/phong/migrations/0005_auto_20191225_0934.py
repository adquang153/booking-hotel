# Generated by Django 2.2.6 on 2019-12-25 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phong', '0004_auto_20191224_1755'),
    ]

    operations = [
        migrations.AddField(
            model_name='phong',
            name='active',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='phong',
            name='loaiphong',
            field=models.IntegerField(choices=[(0, 'Phòng cao cấp Loại 1'), (3, 'Phòng trẻ em'), (1, 'Phòng đơn'), (2, 'Phòng đôi')], default=0),
        ),
    ]