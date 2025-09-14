#!/usr/bin/env python
# Script to set up initial user groups and permissions for the Library Project

import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from bookshelf.models import Book

def setup_groups_and_permissions():
    print("Setting up groups and permissions...")

    # Get content type for the Book model
    book_content_type = ContentType.objects.get_for_model(Book)

    # Get all the permissions for the Book model
    can_view = Permission.objects.get(codename='can_view', content_type=book_content_type)
    can_create = Permission.objects.get(codename='can_create', content_type=book_content_type)
    can_edit = Permission.objects.get(codename='can_edit', content_type=book_content_type)
    can_delete = Permission.objects.get(codename='can_delete', content_type=book_content_type)

    # Create Viewers group
    viewers_group, created = Group.objects.get_or_create(name='Viewers')
    if created:
        print("Created Viewers group")
    viewers_group.permissions.clear()
    viewers_group.permissions.add(can_view)
    print("Added 'can_view' permission to Viewers group")

    # Create Editors group
    editors_group, created = Group.objects.get_or_create(name='Editors')
    if created:
        print("Created Editors group")
    editors_group.permissions.clear()
    editors_group.permissions.add(can_view, can_create, can_edit)
    print("Added 'can_view', 'can_create', and 'can_edit' permissions to Editors group")

    # Create Admins group
    admins_group, created = Group.objects.get_or_create(name='Admins')
    if created:
        print("Created Admins group")
    admins_group.permissions.clear()
    admins_group.permissions.add(can_view, can_create, can_edit, can_delete)
    print("Added 'can_view', 'can_create', 'can_edit', and 'can_delete' permissions to Admins group")

    print("Groups and permissions setup complete!")

if __name__ == "__main__":
    setup_groups_and_permissions()
