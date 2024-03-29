# Generated by Django 2.2.3 on 2019-09-23 05:06

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('todoofz', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('content', models.TextField(blank=True)),
                ('created_date', models.DateField(blank=True, default=django.utils.timezone.now, null=True)),
                ('due_date', models.DateField(blank=True, null=True)),
                ('completed', models.BooleanField(default=False)),
                ('completed_date', models.DateField(blank=True, null=True)),
                ('priority', models.PositiveIntegerField(blank=True, null=True)),
                ('category', models.ForeignKey(default='general', on_delete=django.db.models.deletion.CASCADE, to='todoofz.Category')),
            ],
            options={
                'ordering': ['-created_date'],
            },
        ),
        migrations.DeleteModel(
            name='TodoList',
        ),
    ]
