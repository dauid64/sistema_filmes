from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@method_decorator(
    login_required(login_url='authentication:login', redirect_field_name='next'),
    name='dispatch'
)
class HomeView(TemplateView):
    template_name = 'core/pages/home.html'
