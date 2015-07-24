# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import permission_required

from .utils import sys_call


@csrf_exempt
@require_POST
@permission_required('is_superuser')
def execute_script_view(request):
    source = request.POST.get('source', '').replace('"', r'\"')
    cmd = u'python -c "%s"' % source
    return_code, output = sys_call(cmd.encode('utf-8'))
    output = ('return_code: %i\n\n' % return_code) + output

    return HttpResponse(output)