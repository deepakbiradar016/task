from django.shortcuts import render
import json
from . models import JsonData
from django.contrib import messages

# Create your views here.


def upload_file(request):
    return render(request, 'accounts/upload_file.html')


def record_list(request):

    # Reading uploaded file
    if request.method == 'POST':
        x = request.FILES['data']
        json_data = json.load(x)

        # Validation for the content of the file
        for data in json_data:
            if set(data.keys()) != {'userId', 'id', 'title', 'body'}:
                messages.warning(request, "Data not in proper format")
                return render(request, 'accounts/upload_file.html')

        # validating for duplicate records
        query = JsonData.objects.all()
        if query.exists():
            id_list = []
            for q in query:
                id_list.append(q.id)

            for data in json_data:
                if not data['id'] in id_list:
                    obj = JsonData()
                    obj.userId = data['userId']
                    obj.id = data['id']
                    obj.title = data['title']
                    obj.body = data['body']
                    obj.save()

        else:
            for data in json_data:
                obj = JsonData()
                obj.userId = data['userId']
                obj.id = data['id']
                obj.title = data['title']
                obj.body = data['body']
                obj.save()

        messages.info(request, "Data stored successfully")

    fetch_data = JsonData.objects.all()
    return render(request, 'accounts/record_list.html', {"fetch_data": fetch_data})
