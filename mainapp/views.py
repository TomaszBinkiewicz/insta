from django.shortcuts import render
from django.views import View
from mainapp.models import Image
from django.core.files.storage import FileSystemStorage


class IndexView(View):
    def get(self, request):
        images = Image.objects.all()
        return render(request, 'mainapp/index.html', context={'images': images})


class AddImage(View):
    def get(self, request):
        return render(request, 'mainapp/add_image.html')

    def post(self, request):
        if request.FILES['myfile']:
            myfile = request.FILES['myfile']
            fs = FileSystemStorage()
            filename = fs.save('mainapp/static/mainapp/media/'+myfile.name, myfile)
            uploaded_file_url = fs.url(filename)
            image = Image()
            image.title = request.POST.get('title')
            image.path = myfile.name
            image.user_id = request.POST.get('user')
            image.save()

            return render(request, 'mainapp/add_image.html', context={'path': uploaded_file_url})


class ShowImage(View):
    def get(self, request):
        pass
    def post(self, request):
        pass
