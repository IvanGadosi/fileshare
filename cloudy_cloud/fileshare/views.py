from django.shortcuts import render, redirect, get_object_or_404, reverse
from .models import SharedFile
from .forms import UploadForm
from django.http import HttpResponse, HttpResponseRedirect
import mimetypes
import secrets
from django.contrib.sessions.models import Session


def view_404(request, exception=None):
    return redirect('home')


def home_view(request):
    SharedFile.older_files.filter(paid=False).delete()
    upload_form=UploadForm(initial={"file_key": secrets.token_hex(nbytes=16)})

    session_keys=[]
    for key, value in request.session.items():
        session_keys.append(value)

    if request.method == "POST":
        upload_form = UploadForm(request.POST, request.FILES)
        if upload_form.is_valid():
            uploaded_file=upload_form.save()
            upload_form.save()
            if uploaded_file.file.size > 25000:      #250000000
                uploaded_file.delete()
                return redirect('home')
            else:
                if '{}'.format(uploaded_file.file_key) not in request.session:
                    request.session['{}'.format(uploaded_file.file_key)]='{}'.format(uploaded_file.file_key)
                return redirect('success', uploaded_file.file_key)

    if request.method == "POST":
        searched = request.POST.get('searched')
        file=get_object_or_404(SharedFile, file_key=searched)
        if '{}'.format(file.file_key) not in request.session:
            request.session['{}'.format(file.file_key)]='{}'.format(file.file_key)
        request.session.modified = True
        return redirect('search-result', file.file_key)

    content={
        "upload_form": upload_form,
        'session_keys': session_keys,
    }
    return render(request, "home.html", content)


def success_view(request, pk):
    file=SharedFile.objects.get(file_key=pk)
    content={
        "file": file,
    }
    return render(request, 'success.html', content)


def search_result_view(request, pk):
    file=get_object_or_404(SharedFile, file_key=pk)

    if request.method == "POST":
        with open(file.file.path, 'rb') as f:
            mime_type, _ = mimetypes.guess_type(file.file.path)
            response = HttpResponse(f, content_type=mime_type)
            filename="{}".format(file.file)
            filename=filename[6:]
            response['Content-Disposition'] = "attachment; filename={}".format(filename)
            return response
    content={
        "file": file,
    }
    return render(request, "search_result.html", content)