from django.db import migrations

WAGTAIL_TABLES = [
    # wagtailcore
    "wagtailcore_page",
    "wagtailcore_pagelogentry",
    "wagtailcore_pagesubscription",
    "wagtailcore_pageviewrestriction",
    "wagtailcore_pageviewrestriction_groups",
    "wagtailcore_revision",
    "wagtailcore_referenceindex",
    "wagtailcore_modellogentry",
    "wagtailcore_comment",
    "wagtailcore_commentreply",
    "wagtailcore_site",
    "wagtailcore_locale",
    "wagtailcore_collection",
    "wagtailcore_collectionviewrestriction",
    "wagtailcore_collectionviewrestriction_groups",
    "wagtailcore_groupcollectionpermission",
    "wagtailcore_grouppagepermission",
    "wagtailcore_groupsitepermission",
    "wagtailcore_task",
    "wagtailcore_taskstate",
    "wagtailcore_workflow",
    "wagtailcore_workflowcontenttype",
    "wagtailcore_workflowpage",
    "wagtailcore_workflowstate",
    "wagtailcore_workflowtask",
    "wagtailcore_groupapprovaltask",
    "wagtailcore_groupapprovaltask_groups",
    "wagtailcore_uploadedfile",
    # wagtailadmin
    "wagtailadmin_admin",
    "wagtailadmin_editingsession",
    # wagtailimages
    "wagtailimages_image",
    "wagtailimages_rendition",
    # wagtaildocs
    "wagtaildocs_document",
    # wagtailembeds
    "wagtailembeds_embed",
    # wagtailforms
    "wagtailforms_formsubmission",
    # wagtailredirects
    "wagtailredirects_redirect",
    # wagtailsearch (SQLite FTS variants included — IF EXISTS makes them safe on MySQL)
    "wagtailsearch_indexentry",
    "wagtailsearch_indexentry_fts",
    "wagtailsearch_indexentry_fts_config",
    "wagtailsearch_indexentry_fts_content",
    "wagtailsearch_indexentry_fts_data",
    "wagtailsearch_indexentry_fts_docsize",
    "wagtailsearch_indexentry_fts_idx",
    # wagtailusers
    "wagtailusers_userprofile",
    # taggit (was pulled in by Wagtail)
    "taggit_taggeditem",
    "taggit_tag",
]

WAGTAIL_APPS = [
    "wagtailcore",
    "wagtailadmin",
    "wagtailimages",
    "wagtaildocs",
    "wagtailembeds",
    "wagtailsearch",
    "wagtailforms",
    "wagtailredirects",
    "wagtailusers",
    "wagtailsnippets",
    "wagtail",
    "modelcluster",
    "taggit",
]


def drop_wagtail_tables(apps, schema_editor):
    connection = schema_editor.connection
    vendor = connection.vendor  # 'sqlite' or 'mysql'

    with connection.cursor() as cursor:
        if vendor == "mysql":
            cursor.execute("SET FOREIGN_KEY_CHECKS = 0")
        elif vendor == "sqlite":
            cursor.execute("PRAGMA foreign_keys = OFF")

        quote = "`" if vendor == "mysql" else '"'
        for table in WAGTAIL_TABLES:
            cursor.execute(f"DROP TABLE IF EXISTS {quote}{table}{quote}")

        if vendor == "mysql":
            cursor.execute("SET FOREIGN_KEY_CHECKS = 1")
        elif vendor == "sqlite":
            cursor.execute("PRAGMA foreign_keys = ON")

        # Remove stale migration history entries for removed Wagtail apps.
        # Safe to run — Django ignores apps not in INSTALLED_APPS anyway,
        # but this keeps the migrations table clean.
        placeholders = ", ".join(["%s"] * len(WAGTAIL_APPS))
        cursor.execute(
            f"DELETE FROM django_migrations WHERE app IN ({placeholders})",
            WAGTAIL_APPS,
        )


def noop(apps, schema_editor):
    pass  # irreversible — we can't recreate Wagtail tables on rollback


class Migration(migrations.Migration):

    dependencies = []

    operations = [
        migrations.RunPython(drop_wagtail_tables, reverse_code=noop),
    ]
