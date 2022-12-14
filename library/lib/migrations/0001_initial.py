# Generated by Django 4.0.5 on 2022-07-31 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='borrowed_books',
            fields=[
                ('q', models.AutoField(auto_created=True, editable=False, primary_key=True, serialize=False)),
                ('book_title', models.CharField(max_length=30)),
                ('username', models.CharField(default=True, max_length=100)),
                ('borrower_fname', models.CharField(default=True, max_length=30)),
                ('borrower_lname', models.CharField(default=False, max_length=30)),
                ('borrower_number', models.CharField(default=False, max_length=30)),
                ('book_number', models.CharField(default=False, max_length=30)),
                ('date', models.DateTimeField(default=True)),
                ('Return', models.DateTimeField(default=True)),
                ('fine', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='lib',
            fields=[
                ('Book_number', models.AutoField(auto_created=True, editable=False, primary_key=True, serialize=False)),
                ('Book_name', models.CharField(max_length=30)),
                ('Book_author', models.CharField(max_length=30)),
                ('Book_shelf', models.CharField(max_length=30)),
                ('Number_of_available_copies', models.PositiveIntegerField(null=True)),
                ('Date_added', models.DateTimeField(auto_now_add=True)),
                ('Book_category', models.CharField(max_length=30)),
                ('isbn', models.CharField(default=False, max_length=13, verbose_name='ISBN')),
                ('pic', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
        ),
    ]
