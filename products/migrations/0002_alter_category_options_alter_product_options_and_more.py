# Generated by Django 4.1.2 on 2022-10-25 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['name'], 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['-created'], 'verbose_name_plural': 'Products'},
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='imags/cat-1.jpg', upload_to='imags/'),
        ),
    ]
