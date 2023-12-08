from django.urls import path
from . import views

app_name = 'films'

urlpatterns = [
    path(
        '',
        views.ListFilmsView.as_view(),
        name='list'
    ),
    path(
        'cadastrar',
        views.CreateFilmView.as_view(),
        name='create'
    ),
    path(
        'editar/<int:pk>',
        views.EditFilmView.as_view(),
        name='edit'
    ),
    path(
        'relatorio',
        views.ReportFilms.as_view(),
        name='report'
    ),
    path(
        'export-excel',
        views.ExportFilms.as_view(),
        name='export_excel'
    )
]
