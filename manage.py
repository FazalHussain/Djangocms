#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
<<<<<<< HEAD
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
=======
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "techoryze.settings")
>>>>>>> 07f5f3da0e0bbdb601a04d389a8db007841bb2f3

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
