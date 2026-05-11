from io import BytesIO
from django.template.loader import get_template
try:
    from xhtml2pdf import pisa
except ImportError:
    pisa = None
from django.http import HttpResponse

def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    if pisa:
        pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), result)
        if not pdf.err:
            return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None
