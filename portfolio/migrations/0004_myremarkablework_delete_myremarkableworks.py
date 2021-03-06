# Generated by Django 4.0.2 on 2022-02-12 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_myremarkableworks_delete_resumefile'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyRemarkableWork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('images', models.ImageField(upload_to='media/works')),
                ('works_links', models.URLField(max_length=500)),
            ],
            options={
                'verbose_name_plural': 'MyRemarkableWorks',
            },
        ),
        migrations.DeleteModel(
            name='MyRemarkableWorks',
        ),
    ]
