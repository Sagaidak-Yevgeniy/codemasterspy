from django.contrib import admin
from .models import Certificate

@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'issued_date')
    verbose_name = 'Сертификат'
    verbose_name_plural = 'Сертификаты'

