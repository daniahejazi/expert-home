import os
import sys

# Assuming your Django project's name is 'myproject',
# and it is located in the same directory as this script.
# Adjust the path and project name as necessary.
project_home = os.path.dirname(__file__)
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
