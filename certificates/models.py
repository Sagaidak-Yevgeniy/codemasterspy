import qrcode
from io import BytesIO
from django.core.files.base import ContentFile
from django.db import models
from django.urls import reverse

class Certificate(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    issued_date = models.DateField()
    qr_code = models.ImageField(upload_to='qr_codes/', blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """
        Возвращает путь к странице сертификата.
        """
        return reverse('certificate_detail', args=[str(self.id)])

    def save(self, *args, **kwargs):
        """
        Генерация QR-кода после сохранения объекта.
        """
        super().save(*args, **kwargs)  # Сначала сохраняем объект

        # Генерация полного URL
        full_url = f"https://codemasterspy-git-main-yevgeniys-projects-9a9cdb4d.vercel.app/{self.get_absolute_url()}"

        # Создание QR-кода
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(full_url)
        qr.make(fit=True)

        # Сохранение QR-кода в изображение
        img = qr.make_image(fill_color="black", back_color="white")
        buffer = BytesIO()
        img.save(buffer, format="PNG")

        # Сохранение QR-кода в поле модели
        file_name = f"certificate_{self.id}_qr.png"
        self.qr_code.save(file_name, ContentFile(buffer.getvalue()), save=False)

        super().save(*args, **kwargs)  # Сохраняем объект снова
