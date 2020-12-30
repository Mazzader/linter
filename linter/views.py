from uuid import uuid4

from django.shortcuts import render
from django.template import RequestContext
from django.template.context_processors import csrf
from django.views import View
from django.views.decorators.csrf import csrf_protect, csrf_exempt

from .linter import handle_uploaded_file, linter_handler


class IndexView(View):
    template_name = 'index.html'

    def get(self, request):
        return render(request, self.template_name)


class LinterView(View):
    template_name = 'linter.html'

    @csrf_exempt
    def get(self, request):
        cdict = {}
        cdict.update(csrf(request))
        return render(request, self.template_name, context=cdict, context_instance=RequestContext(request))

    @csrf_exempt
    def post(self, request):
        uuid = uuid4()
        print(request.FILES.keys())
        handle_uploaded_file(request.FILES['file'], uuid)
        with open("{uuid}.txt".format(uuid)) as file_handler:
            res = linter_handler(linter_handler)
            print(res)
        return render(request, self.template_name,)