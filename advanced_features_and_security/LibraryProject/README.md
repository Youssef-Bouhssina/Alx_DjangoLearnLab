# LibraryProject
# Library Project - Advanced Features and Security

A Django application that demonstrates the implementation of permissions and groups for access control.

## Permissions and Groups System

### Custom Permissions

The Book model has the following custom permissions:

- `can_view`: Allows users to view detailed information about books
- `can_create`: Allows users to add new books to the system
- `can_edit`: Allows users to modify existing book information
- `can_delete`: Allows users to remove books from the system

### User Groups

The application defines three user groups with specific permission sets:

1. **Viewers**
   - Permissions: `can_view`
   - Can view book details but cannot make any changes

2. **Editors**
   - Permissions: `can_view`, `can_create`, `can_edit`
   - Can view, add, and modify books but cannot delete them

3. **Admins**
   - Permissions: `can_view`, `can_create`, `can_edit`, `can_delete`
   - Have full control over book management

## Setting Up Groups and Permissions

A utility script is provided to set up the initial groups and permissions:

```bash
python setup_groups.py
```

This script will create the necessary groups and assign the appropriate permissions to each group.

## Enforcing Permissions in Views

Permissions are enforced in views using Django's permission system:

- Class-based views use `PermissionRequiredMixin` to check for specific permissions
- Function-based views use the `@permission_required` decorator
- Templates conditionally display UI elements based on user permissions using `{% if perms.bookshelf.can_edit %}` style checks

## Testing the Permission System

To test the permission system:

1. Create test users in the Django admin
2. Assign these users to different groups (Viewers, Editors, Admins)
3. Log in as each user and verify that they can only perform actions allowed by their group's permissions

## Implementation Details

- Permission checks are implemented in all relevant views
- Templates conditionally render UI elements based on user permissions
- Custom error messages are displayed when users attempt unauthorized actions
This is a basic Django project for learning purposes.
