from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from .models import Person

def person_list(request):
    persons = Person.objects.all()
    return render(request, 'person_list.html', {'persons': persons})

def generate_pdf(request):
    template_path = 'pdf_template.html'
    persons = Person.objects.all()
    context = {'persons': persons}

    # Generate PDF using the template
    template = get_template(template_path)
    html = template.render(context)
    pdf = generate_pdf_from_html(html)

    # Return the PDF as a response
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="persons.pdf"'
    response.write(pdf)

    return response

def preview_pdf(request):
    template_path = 'pdf_template.html'
    persons = Person.objects.all()
    context = {'persons': persons}

    # Render the template to HTML
    template = get_template(template_path)
    html = template.render(context)

    return HttpResponse(html)

def generate_pdf_from_html(html):
    result = BytesIO()
    pdf = pisa.CreatePDF(BytesIO(html.encode('UTF-8')), result)

    if not pdf.err:
        return result.getvalue()
    else:
        return HttpResponse('An error occurred while generating PDF')