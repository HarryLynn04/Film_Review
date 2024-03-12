# Generated by Django 2.2.28 on 2024-03-12 12:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Film_Review', '0002_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='film_images/'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Rating', models.IntegerField()),
                ('Likes', models.IntegerField()),
                ('DatePublished', models.DateField()),
                ('Description', models.CharField(max_length=1000)),
                ('Film', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Film_Review.Film')),
                ('Username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
