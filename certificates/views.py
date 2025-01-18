from django.shortcuts import render, get_object_or_404
from .models import Certificate

def certificate_detail(request, pk):
    """
    Отображение страницы с данными сертификата.
    """
    certificate = get_object_or_404(Certificate, pk=pk)
    return render(request, 'certificates/certificate_detail.html', {'certificate': certificate})
