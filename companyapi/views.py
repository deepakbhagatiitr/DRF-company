from django.http import JsonResponse

def home(request):
    data = {"message": "Hello World"}
    return JsonResponse(data)
