# Generated by Django 2.2.7 on 2019-11-08 13:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.TextField(max_length=20)),
                ('password', models.TextField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('title', models.TextField(max_length=64)),
                ('path', models.TextField(max_length=64)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.User')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('content', models.TextField(max_length=255)),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Image')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.User')),
            ],
        ),
    ]