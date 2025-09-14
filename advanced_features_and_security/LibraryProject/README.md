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
# Library Project - Custom User Model Implementation

This Django project demonstrates the implementation of a custom user model with additional fields and functionality.

## Custom User Model

The project replaces Django's default user model with a custom implementation that includes additional fields:

- `date_of_birth`: A date field for storing the user's birth date
- `profile_photo`: An image field for storing the user's profile picture

## Project Structure

- **accounts**: Contains the custom user model implementation
  - `models.py`: Defines CustomUser and CustomUserManager
  - `admin.py`: Configures the admin interface for CustomUser
- **bookshelf**: Contains the Book model and related views
- **settings.py**: Configured to use the custom user model

## Implementation Details

### Custom User Model

The custom user model extends Django's `AbstractUser` class to inherit all the standard user fields and functionality while adding custom fields:

```python
class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)

    objects = CustomUserManager()

    def __str__(self):
        return self.username
```

### Custom User Manager

A custom user manager is implemented to handle user creation and administrative tasks:

```python
class CustomUserManager(BaseUserManager):
    def create_user(self, username, email=None, password=None, **extra_fields):
        # Implementation for creating regular users

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        # Implementation for creating admin users
```

### Settings Configuration

The project's settings.py includes the necessary configuration to use the custom user model:

```python
INSTALLED_APPS = [
    # ...
    'accounts',
    # ...
]

AUTH_USER_MODEL = 'accounts.CustomUser'
```

### Admin Interface

The Django admin interface is configured to properly display and manage the custom user model:

```python
class CustomUserAdmin(UserAdmin):
    # Configuration for admin interface
```

## Usage

When working with the custom user model in your application:

1. Import the user model using Django's get_user_model function:
   ```python
   from django.contrib.auth import get_user_model
   User = get_user_model()
   ```

2. Or use the settings reference in foreign keys:
   ```python
   from django.conf import settings

   class Profile(models.Model):
       user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
   ```

This approach ensures your application remains compatible if the user model changes.