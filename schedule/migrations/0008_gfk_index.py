from django.db import migrations, models
from django.db.migrations import AddIndex


class Migration(migrations.Migration):

    dependencies = [
        ("contenttypes", "0002_remove_content_type_name"),
        ("schedule", "0007_merge_text_fields"),
    ]

    operations = [
        migrations.AlterField(
            model_name="calendarrelation",
            name="object_id",
            field=models.IntegerField(db_index=True),
        ),
        migrations.AlterField(
            model_name="eventrelation",
            name="object_id",
            field=models.IntegerField(db_index=True),
        ),
        AddIndex("calendarrelation", models.Index(fields=["content_type", "object_id"], name="event_start_end_idx11"),),
        AddIndex("eventrelation", models.Index(fields=["content_type", "object_id"], name="event_start_end_idx12"),
        ),
        migrations.AlterField(
            model_name="calendar",
            name="slug",
            field=models.SlugField(verbose_name="slug", max_length=200, unique=True),
        ),
    ]
