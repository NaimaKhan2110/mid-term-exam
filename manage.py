import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "event_management.settings")

    # Get the port from environment variables (default is 8000)
    port = os.environ.get("PORT", "8000")

    # Check if running locally or in a cloud environment
    if "RENDER" in os.environ or "AWS" in os.environ or "PRODUCTION" in os.environ:
        bind_address = "0.0.0.0"  # For cloud servers (Render, AWS, etc.)
    else:
        bind_address = "127.0.0.1"  # For local development

    from django.core.management import execute_from_command_line
    execute_from_command_line([sys.argv[0], "runserver", f"{bind_address}:{port}"])
