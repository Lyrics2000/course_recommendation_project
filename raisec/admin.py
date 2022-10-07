from django.contrib import admin

# Register your models here.

from .models import (
    RaisecGroup,
    RaisecQuestions
)


admin.site.register(RaisecGroup)
admin.site.register(RaisecQuestions)