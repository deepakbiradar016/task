from django.shortcuts import render , redirect
import json
from . models import JsonData
from django.contrib import messages

# Create your views here.


def upload_file(request):
    return render(request, 'accounts/upload_file.html')


def record_list(request):

    if request.method == 'POST':
        x = request.FILES['data']
        json_data = json.load(x)

        for data in json_data:
            if set(data.keys()) != {'userId', 'id', 'title', 'body'}:
                messages.warning(request, "Data not in proper format")
                return render(request, 'accounts/upload_file.html')

        query = JsonData.objects.all()
        if query.exists():
            query_id = []
            for q in query:
                query_id.append(q.id)

            for data in json_data:
                if not data['id'] in query_id:
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
