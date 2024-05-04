from django.db import models
from django.utils import timezone



class DiaryNote(models.Model):
    TEXT_DESCRIPTION_MAX_LENGTH = 255
    REASON_CHOICES = [
        ('Голод', 'Голод'),
        ('Скука', 'Скука'),
        ('За компанию', 'За компанию'),
        ('Стресс', 'Стресс'),
        ('По расписанию', 'По расписанию'),
        ('Привычка', 'Привычка'),
        ('Еда была рядом', 'Еда была рядом'),
    ]
    FEELINGS_CHOICES = [
        ('Приятное чувство насыщения', 'Приятное чувство насыщения'),
        ('Тяжесть', 'Тяжесть'),
        ('Чувство вины, стыда', 'Чувство вины, стыда'),
        ('Жалею о приеме пищи', 'Жалею о приеме пищи'),
        ('Дискомфорт (вздутие, колики и прочее)', 'Дискомфорт (вздутие, колики и прочее)'),
        ('Пустота', 'Пустота'),
    ]
    tg_user_id = models.CharField(max_length=20, null=True)
    text_description = models.CharField(max_length=TEXT_DESCRIPTION_MAX_LENGTH)
    time = models.TimeField(default=timezone.now)
    photo = models.ImageField(upload_to='diary_photos/', null=True, blank=True)
    level_before = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)], null=True, blank=True)
    reason_of_eat = models.CharField(max_length=50, choices=REASON_CHOICES)
    level_after = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)], null=True, blank=True)
    feelings_after_eating = models.CharField(max_length=50, choices=FEELINGS_CHOICES)
    comment = models.TextField()