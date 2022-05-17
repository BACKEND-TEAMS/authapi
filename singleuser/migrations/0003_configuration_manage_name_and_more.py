# Generated by Django 4.0.3 on 2022-05-16 08:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('singleuser', '0002_alter_college_student_owner_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='configuration_manage',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='college_student',
            name='add_previous_education',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='college_student',
            name='collage_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='college_student',
            name='course_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='college_student',
            name='owner',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='college', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='college_student',
            name='specification_in',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='configuration_manage',
            name='add_skills',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='configuration_manage',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='configuration_manage',
            name='image',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='configuration_manage',
            name='owner',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='configure', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='employed',
            name='add_previous_education',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='employed',
            name='company_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='employed',
            name='owner',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employed', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='employed',
            name='position_in_company',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='school_student',
            name='academy_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='school_student',
            name='current_qualification',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='school_student',
            name='qualification_status',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]