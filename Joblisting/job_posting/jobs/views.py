from django.shortcuts import render, redirect
from .models import Job, UserInterest
from .forms import UserInterestForm

def job_list(request):
    jobs = Job.objects.all()
    return render(request, 'job_list.html', {'jobs': jobs})

def job_detail(request, job_id):
    job = Job.objects.get(id=job_id)
    form = UserInterestForm()
    if request.method == 'POST':
        form = UserInterestForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('job_list')
    return render(request, 'job_detail.html', {'job': job, 'form': form})

def upload_job(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        location = request.POST['location']
        Job.objects.create(title=title, description=description, location=location)
        return redirect('job_list')
    return render(request, 'upload_job.html')
