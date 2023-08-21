# Generated by Django 4.2.1 on 2023-08-21 07:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0002_doctor_info_address_doctor_info_age_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='doctorExperience',
            fields=[
                ('experience_id', models.AutoField(primary_key=True, serialize=False)),
                ('work_place', models.CharField(max_length=200)),
                ('from_year', models.DateField()),
                ('to_year', models.DateField(blank=True, null=True)),
                ('designation', models.CharField(max_length=200)),
                ('doctor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctors.doctor_info')),
            ],
        ),
        migrations.CreateModel(
            name='DoctorEducation',
            fields=[
                ('education_id', models.AutoField(primary_key=True, serialize=False)),
                ('degree', models.CharField(max_length=200)),
                ('institute', models.CharField(max_length=200)),
                ('year_of_completion', models.DateField()),
                ('doctor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctors.doctor_info')),
            ],
        ),
    ]
