from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import DiaryNoteForm
import datetime

months_russian = [
    "Январь",
    "Февраль",
    "Март",
    "Апрель",
    "Май",
    "Июнь",
    "Июль",
    "Август",
    "Сентябрь",
    "Октябрь",
    "Ноябрь",
    "Декабрь"
]


def form_view(request):
    # user_id = request.GET.get('user_id')
    if request.method == 'POST':
        form = DiaryNoteForm(request.POST, request.FILES)
        if form.is_valid():
            # form.save()
            data = form.save(commit=False)
            data.tg_user_id = request.GET.get('tg_user_id')
            data.save()
            return redirect('google.com')
    else:
        form = DiaryNoteForm(initial={'user_id': request.GET.get('tg_user_id')})
    offset = datetime.timezone(datetime.timedelta(hours=3))
    datetime_now = datetime.datetime.now(offset)
    return render(request, 'myapp/form.html',
                  {'form': form, 'datetime': datetime_now, 'month': months_russian[datetime_now.month]})
