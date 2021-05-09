from django.views.generic import TemplateView
from django.http import HttpResponse


# Homepage
class HomePage(TemplateView):
    """
       This method is used for serving index page.
       :param request: it's a HttpResponse from user.
       :type request: HttpResponse.
       :return: this method returns a saving apartment form which is a HTML page.
       :rtype: HttpResponse.
    """
    template_name = 'index.html'
