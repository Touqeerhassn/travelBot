from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from .ml_module import responses

@csrf_exempt
# @require_POST
def chat_api(request):
    try:
        user_input = request.POST.get('user_input')
        response = responses(str(user_input))
        return JsonResponse({'response': response})

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


# def check_api(request):
#     return HttpResponse("this is response")

