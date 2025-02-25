from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Job, JobApplication
from .forms import JobForm, ApplicationForm
from django.http import HttpResponse
from .forms import JobApplicationForm
def job_list(request):
    jobs = Job.objects.filter(is_active=True)
    return render(request, 'jobs/job_list.html', {'jobs': jobs})

def job_detail(request, pk):
    job = get_object_or_404(Job, pk=pk)
    return render(request, 'jobs/job_detail.html', {'job': job})








def apply_job(request, pk):
    job = get_object_or_404(Job, pk=pk)  # Get the job by ID
    if request.method == 'POST':
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save(commit=False)
            application.job = job
            application.save()
            # Redirect to the success page after the application is submitted
            return redirect('application_success')
    else:
        form = JobApplicationForm()

    return render(request, 'jobs/apply_job.html', {'form': form, 'job': job})




def application_success(request):
    return render(request, 'jobs/application_success.html')


@login_required
def add_job(request):
    if not request.user.is_staff:
        return redirect('job_list')
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('job_list')
    else:
        form = JobForm()
    return render(request, 'jobs/add_job.html', {'form': form})
