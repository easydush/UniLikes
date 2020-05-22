import json

from django.http import JsonResponse, HttpResponse, HttpResponseBadRequest
from django.views.generic import FormView


class AjaxFormMixin(FormView):
    template_name = 'voting/rate_form.html'
    """
    Mixin to add AJAX support to a form.
    Must be used with an object-based FormView (e.g. CreateView)
    """

    def form_valid(self, form):
        form.save()
        return HttpResponse('OK')

    def form_invalid(self, form):
        errors_dict = json.dumps(dict([(k, [e for e in v]) for k, v in form.errors.items()]))
        return HttpResponseBadRequest(json.dumps(errors_dict))
