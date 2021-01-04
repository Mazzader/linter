from uuid import uuid4

from django.shortcuts import render
from django.template import RequestContext
from django.template.context_processors import csrf
from django.views import View
from django.views.decorators.csrf import csrf_protect, csrf_exempt

from .forms import JsFileForm
from .linter import main_linter
from .models import Code, StatusCode


class IndexView(View):
    template_name = 'index.html'

    def get(self, request):
        return render(request, self.template_name)


class LinterView(View):
    template_name = 'linter.html'
    success_template = 'success.html'
    failed_template = 'failed.html'

    def get(self, request):
        if request.method == 'GET':
            form = JsFileForm()
            cdict = {
                'form': form
            }
            cdict.update(csrf(request))
            return render(request, self.template_name, context=cdict)

    def post(self, request):
        if request.method == 'POST':
            form = JsFileForm(request.POST, request.FILES)
            cdict = {
                'form': form
            }
            cdict.update(csrf(request))
            print(form.is_valid(), request.FILES)
            if form.is_valid():
                test = main_linter(request.FILES['docfile'])
                if len(test) == 0:
                    return render(request, self.success_template)
                else:
                    res = ''
                    for k, v in test.items():
                        res = res + k + str(v) + '\n'
                    failed_test = Code(status=100, errors=res, statuscode=StatusCode.objects.get(code=101))
                    failed_test.save()
                    return render(request, self.failed_template, context={'fail':res.split(']')})

        return render(request, self.template_name, )

class AllTests(View):
    template_name = 'all_tests.html'

    def get(self, request):
        if request.method == 'GET':
            return render(request, self.template_name, context={'tests': Code.objects.all()})