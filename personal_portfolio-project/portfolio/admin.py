from django.contrib import admin
#import for .models what the project name is. In this case, its called project.
from.models import Project
#link the models page for project to the admin.py in personal portfolio folder
admin.site.register(Project)
