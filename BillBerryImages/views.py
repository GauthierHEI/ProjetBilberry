
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views.decorators.csrf import csrf_exempt

from .models import Image
from .forms import ImageForm


def index(request):
    return render(request, 'BillBerryImages/index.html')


def image_list_view(request):
    image_list = Image.objects.order_by('id')
    context = {
        'images': image_list
    }
    return render(request, 'BillBerryImages/image.html', context)


def image_viewer_view(request):
    image_list = Image.objects.order_by('id')
    context = {
        'images': image_list
    }
    return render(request, 'BillBerryImages/image_viewer.html', context)


def image_uploader_view(request):
    form = ImageForm()
    validation = ""
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            validation = "Votre image est enregistrée"
    context = {'form': form,
               'validation': validation}
    return render(request, 'BillBerryImages/image_uploader.html', context)


@csrf_exempt
def image_update_view(request):
    print("Update")
    if request.method == 'POST':
        image_id = request.POST.get('id')
        update = request.POST.get('update')
        data = {
            'id': image_id,
            'update': update
        }
        if update == "rejected":
            image = Image.objects.get(pk=image_id)
            image.verified = True
            image.rejected = True
            image.save()
        else:
            image = Image.objects.get(pk=image_id)
            image.verified = True
            image.rejected = False
            image.save()

    return JsonResponse(data)
