from django.views.generic import TemplateView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@method_decorator(
    login_required(login_url='authentication:login', redirect_field_name='next'),
    name='dispatch'
)
class HomeView(TemplateView):
    template_name = 'core/pages/home.html'

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(**kwargs)
        task_id = self.request.session.get('task_id', None)
        export_request_id = self.request.session.get('export_request_id')
        if self.request.session.get('task_id', None):
            ctx.update(
                {
                    'task_id': task_id,
                    'export_request_id': export_request_id
                }
            )
        return ctx
