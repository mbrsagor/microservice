from gettext import gettext as _

# User Service Integration Messages
USER_NOT_FOUND = _("User not found in User Service")
UNAUTHORIZED_USER_FETCH = _("Not authorized to fetch this user info")
USER_SERVICE_ERROR = _("Error communicating with User Service")

# Note: Using standard f-string formatting for this one at call site
USER_SERVICE_UNAVAILABLE = _("User Service is unavailable: {exc}")

# API Validation Messages
INVALID_AUTH_HEADER = _("Invalid authorization header format")
NOT_DOCTOR_ROLE = _("User role is not assigned as doctor")
DOCTOR_ALREADY_EXISTS = _("Doctor profile already exists for this user")
DOCTOR_NOT_FOUND = _("Doctor not found")
