#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

import environment


def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "StudentTrackingSystem.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    if "test" in sys.argv or os.environ.get("USE_LOCAL_CONFIGS") == "TRUE":
        environment.local_config = True
        environment.local_prereq = True
        print("Using local config files")

    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
