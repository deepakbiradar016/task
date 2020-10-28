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


class RecordList(LoginRequiredMixin, ListView):
    model = JsonData
    template_name = 'accounts/record_list.html'
    queryset = JsonData.objects.all()
    paginate_by = 30

    def post(self, *args, **kwargs):
        # Reading uploaded file
        x = self.request.FILES['data']
        json_data = json.load(x)

        # Validation for the content of the file
        for data in json_data:
            if set(data.keys()) != {'userId', 'id', 'title', 'body'}:
                messages.warning(self.request, "Data not in proper format")
                return redirect('/accounts/upload-file/')

        # validating for duplicate records
        query = JsonData.objects.all()
        if query.exists():
            id_list = [q.id for q in query]
            # id_list = []
            # for q in query:
            #     id_list.append(q.id)

            for data in json_data:
                if not data['id'] in id_list:
                    obj = JsonData.objects.create(id=data['id'], userId=data['userId'], itle=data['title'], body=data['body'])

        else:
            for data in json_data:
                obj = JsonData.objects.create(id=data['id'], userId=data['userId'], title=data['title'], body=data['body'])

        messages.info(self.request, "Data stored successfully")
        return redirect('/accounts/record-list2/')
