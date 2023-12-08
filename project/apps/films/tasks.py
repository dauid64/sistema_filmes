from celery import shared_task
from django.utils import timezone
from .models import FilmExportRequest, Film, FilmImportRequest
from django.contrib.auth.models import User
from unidecode import unidecode
import io
import pandas as pd
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


@shared_task
def import_excel_to_films(import_request_id):
    import_request = FilmImportRequest.objects.get(pk=import_request_id)
    user = import_request.user

    df = pd.read_excel(import_request.report.path)

    df.columns = [unidecode(col.lower().replace(' ', '_')) for col in df.columns]

    df['gostaria_de_assistir'] = df['gostaria_de_assistir'].apply(lambda x: x.lower())

    df['gostaria_de_assistir'] = df['gostaria_de_assistir'].replace(
        {
            'assistido': False,
            'gostaria': True
        }
    )

    # df['assistido_em'] = pd.to_datetime(df['assistido_em'], format='%d/%m/%Y', errors='coerce')
    df['assistido_em'] = df['assistido_em'].replace({pd.NaT: None})

    for row in df.itertuples(index=False):
        Film.objects.create(
            user=user,
            name=getattr(row, 'nome'),
            description=getattr(row, 'descricao'),
            assisted_in=getattr(row, 'assistido_em', None),
            would_like=getattr(row, 'gostaria_de_assistir')
        )
