from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.ForeignKey(
                to='blog.Category',
                null=True,
                blank=True,
                on_delete=django.db.models.deletion.SET_NULL,
            ),
        ),
    ]
