
from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'index.html'
    from .models import Curso

    class IndexView(TemplateView):
        template_name = 'index.html'

        def get_context_data(self, **kwargs):
            context = super(IndexView, self).get_context_data(**kwargs)
            context['cursos'] = Curso.objects.order_by('?').all()
            return context


class SobreView(TemplateView):
    template_name = 'about-us.html'



