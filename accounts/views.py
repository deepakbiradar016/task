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

        query = JsonData.objects.all()

        if query.exists():
            for data in json_data:
                for q in query:
                    print(q.id,'yesssssssssssssssssssssssss')
            # for q in query:
            #     for data in json_data:
            #         if q.userId == data['userId'] and q.json_id == data['id'] and q.title == data['title'] and q.body == data['body']:
            #             continue
            #         else:
            #             obj = JsonData()
            #             obj.userId = data['userId']
            #             obj.id = data['id']
            #             obj.title = data['title']
            #             obj.body = data['body']
            #             obj.save()
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
