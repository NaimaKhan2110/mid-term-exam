import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "event_management.settings")
    
    # Get the port from the environment variable (default 8000)
    port = os.environ.get("PORT", "8000")

    from django.core.management import execute_from_command_line
    execute_from_command_line([sys.argv[0], "runserver", f"0.0.0.0:{port}"])
