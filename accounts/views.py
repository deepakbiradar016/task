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

        print(query[0].id, json_data[0]['id'], 'qqqqqqqqqqq')

        if query.exists():
            for data in json_data:
                for q in query:
                    pass

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



















# obj = JsonData()
# obj.user = request.user
# obj.userId = data['userId']
# obj.json_id = data['id']
# obj.title = data['title']
# obj.body = data['body']
# obj.save()
# return redirect("/")
