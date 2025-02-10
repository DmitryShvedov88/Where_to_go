from django.template import loader
from django.http import HttpResponse


def show_phones(request):
    template = loader.get_template('index.html')
    context = {}
    rendered_page = template.render(context, request)
    return HttpResponse(rendered_page)
