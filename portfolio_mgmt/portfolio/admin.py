from django.contrib import admin
from .models import Skill, Portfolio, Projects, Category
# Register your models here.
admin.site.register(Category)
admin.site.register(Skill)
admin.site.register(Portfolio)
admin.site.register(Projects)