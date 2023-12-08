from celery import shared_task
from django.utils import timezone
from .models import FilmExportRequest, Film
import io
import xlwt


@shared_task
def export_films_excel(film_export_request_id):
    film_export_request = FilmExportRequest.objects.get(
        pk=film_export_request_id)
    film_export_request.started_at = timezone.now()
    film_export_request.save()

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Filmes')

    row_num = 0
    columns = ['Id', 'Nome', 'Descrição', 'Gostaria de Assistir']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num])

    row_num = 1
    for film in Film.objects.filter(user=film_export_request.user):
        ws.write(row_num, 0, film.id)
        ws.write(row_num, 1, film.name)
        ws.write(row_num, 2, film.description)
        ws.write(
            row_num, 3,
            'Gostaria' if film.would_like is True else 'Assistido'
        )
        row_num += 1
    
    output = io.BytesIO()
    wb.save(output)

    film_export_request.report.save(
        f'films_{film_export_request.user.username}.xlsx', output
    )
    film_export_request.finished_at = timezone.now()
    film_export_request.save()
