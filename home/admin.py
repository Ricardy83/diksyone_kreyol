from django.contrib import admin
from .models import *


admin.site.register(Mot)
admin.site.register(Synonyme)
admin.site.register(Antonyme)
admin.site.register(Expression)