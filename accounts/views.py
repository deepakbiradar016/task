from django.shortcuts import render, redirect
import json
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from . models import JsonData
from django.contrib import messages
from django.views.generic import ListView
# Create your views here.


@login_required
def upload_file(request):
    return render(request, 'accounts/upload_file.html')

@login_required
def record_list(request):

    # Reading uploaded file
    if request.method == 'POST':
        x = request.FILES['data']
        json_data = json.load(x)

        # Validation for the content of the file
        for data in json_data:
            if set(data.keys()) != {'userId', 'id', 'title', 'body'}:
                messages.warning(request, "Data not in proper format")
                return redirect('/accounts/upload-file/')

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

    # fetch_data = JsonData.objects.all()
    return redirect('/accounts/record-list2/')


class RecordList(LoginRequiredMixin, ListView):
    model = JsonData
    template_name = 'accounts/record_list.html'
    queryset = JsonData.objects.all()
    paginate_by = 30

