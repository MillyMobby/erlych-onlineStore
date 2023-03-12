# Generated by Django 4.1.4 on 2023-02-14 00:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=255)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('picture', models.ImageField(upload_to='images/')),
                ('biography', models.TextField(blank=True)),
            ],
            options={
                'verbose_name_plural': 'artists',
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=255)),
                ('slug', models.SlugField(max_length=255, unique=True)),
            ],
            options={
                'verbose_name_plural': 'genres',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('summary', models.TextField(blank=True)),
                ('overview', models.TextField(blank=True)),
                ('cover', models.ImageField(upload_to='images/')),
                ('slug', models.SlugField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=4)),
                ('available', models.BooleanField(default=True)),
                ('is_active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='admin_creator', to=settings.AUTH_USER_MODEL)),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='store.artist')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='store.genre')),
            ],
            options={
                'verbose_name_plural': 'Products',
                'ordering': ('-created',),
            },
        ),
    ]