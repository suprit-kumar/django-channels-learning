from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

def index(request):
    return render(request,'index.html',context={'text':'Hello User'})

@csrf_exempt
def test(request):
    print(request)
    return JsonResponse({'msg':'success'})

@csrf_exempt
def test_connection(request):
    data = request.POST['app']
    print(data)

    return JsonResponse({'status':200})