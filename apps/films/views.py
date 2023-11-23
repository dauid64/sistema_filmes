from typing import Any
from .models import Film
from django.views.generic import ListView, CreateView, \
    UpdateView, View
from django.http import JsonResponse
from .forms import FilmForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponse
from django.core.paginator import Paginator
import xlwt


@method_decorator(
    login_required(login_url='authentication:login', redirect_field_name='next'),
    name='dispatch'
)
class ListFilmsView(ListView):
    template_name = 'films/pages/list.html'
    model = Film
    context_object_name = 'films'

    def get_queryset(self):
        qs = super().get_queryset()
        search = self.request.GET.get('search', None)
        qs = qs.filter(user=self.request.user).order_by('-id')
        if search:
            qs = qs.filter(
                name__icontains=search
            )
        return qs

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(**kwargs)
        additional_url_query = ''
        paginator = Paginator(ctx['films'], 10)
        page_number = self.request.GET.get('page', 1)
        page_obj = paginator.get_page(page_number)
        pagination_range = paginator.get_elided_page_range(page_number)
        ctx.update(
            {
                'films': page_obj,
                'paginator': paginator,
                'pagination_range': pagination_range,
                'additional_url_query': additional_url_query

            }
        )
        return ctx


@method_decorator(
    login_required(login_url='authentication:login', redirect_field_name='next'),
    name='dispatch'
)
class CreateFilmView(CreateView):
    model = Film
    form_class = FilmForm
    template_name = 'films/pages/create.html'
    success_url = reverse_lazy('films:list')

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        instance.save()
        return super().form_valid(form)


@method_decorator(
    login_required(login_url='authentication:login', redirect_field_name='next'),
    name='dispatch'
)
class EditFilmView(UpdateView):
    model = Film
    form_class = FilmForm
    template_name = 'films/pages/edit.html'
    success_url = reverse_lazy('films:list')


@method_decorator(
    login_required(login_url='authentication:login', redirect_field_name='next'),
    name='dispatch'
)
class ReportFilms(View):
    def get(self, request):
        would_like_films = Film.objects.filter(would_like=True, user=request.user).count()
        assisted_films = Film.objects.filter(would_like=False, user=request.user).count()
        return JsonResponse(
            data={
                'data': [would_like_films, assisted_films]
            }
        )


@method_decorator(
    login_required(login_url='authentication:login', redirect_field_name='next'),
    name='dispatch'
)
class ExportFilms(View):
    def get(self, request):
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="relatorio.xls"'

        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('Filmes')

        row_num = 0

        columns = ['Id', 'Nome', 'Descrição', 'Gostaria de Assistir']

        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num])

        films = Film.objects.filter(user=request.user)

        row_num = 1
        for film in films:
            ws.write(row_num, 0, film.id)
            ws.write(row_num, 1, film.name)
            ws.write(row_num, 2, film.description)
            ws.write(row_num, 3,
                     'Gostaria' if film.would_like is True else 'Assistido')
            row_num += 1

        wb.save(response)
        return response
