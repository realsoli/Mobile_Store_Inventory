import os
import sys


def main():

    if os.environ.get('DJANGO_ENV') == 'production':
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Mobile_Store_Inventory.settings.production")
    else:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Mobile_Store_Inventory.settings.development")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()