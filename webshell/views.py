# -*- coding: utf-8 -*-

import commands

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import permission_required


@csrf_exempt
@require_POST
@permission_required('is_superuser')
def execute_script_view(request):
    source = request.POST.get('source', '').replace('"', r'\"')
    cmd = u'python -c "%s"' % source
    result = commands.getoutput(cmd.encode('utf-8'))

    return HttpResponse(result)