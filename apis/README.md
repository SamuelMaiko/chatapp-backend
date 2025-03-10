# APIs Directory

This app generalizes all app URLs to avoid congestion in the main `urls.py` file. Each app's URLs are included here.

## URL Structure

The main `urls.py` file includes the base path `api/` for this app. Each app then appends its specific paths to this base path.

### Example

- **Profile App**: The `a_profile` app handles all profile-related operations.
  - Base path: `api/profile/`
  - Defined in `a_profile/urls.py`.

## Common Code

This folder also contains common code like `BaseModel` to avoid repeating fields like `created_at` and `updated_at`.

### Example URL Inclusion

```python
from django.urls import path, include

urlpatterns = [
    path('auth/', include('a_authentication.urls')),
    path('profile/', include('a_profile.urls')),
    # ...other app urls...
]
```
