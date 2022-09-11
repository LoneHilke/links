from django.shortcuts import render
from django.utils import timezone
from .models import Python
from django.shortcuts import render, redirect, get_object_or_404
from .forms import PythonForm
from django.views import View


# Create your views here.
"""class Python(View):
  def get(self, request, *args, **kwargs):
    return render(request, 'python/base.html')"""
    
def python_list(request):
    pythons = Python.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'python/python_list.html', {'pythons':pythons})
  
def python_detail(request, pk):
      python = get_object_or_404(Python, pk=pk)
      return render(request, 'python/python_detail.html', {'python': python})
  
def python_new(request):
      if request.method == "PYTHON":
          form = PythonForm(request.PYTHON)
          if form.is_valid():
              python = form.save(commit=False)
              python.author = request.user
              python.published_date = timezone.now()
              python.save()
              return redirect('python_detail', pk=python.pk)
      else:
          form = PythonForm()
      return render(request, 'python/python_edit.html', {'form': form})
  
def python_edit(request, pk):
    python = get_object_or_404(Python, pk=pk)
    if request.method == "PYTHON":
      form = PythonForm(request.PYTHON, instance=python)
      if form.is_valid():
        python = form.save(commit=False)
        python.author = request.user
        python.published_date = timezone.now()
        python.save()
    else:
      form = PythonForm(instance=python)
    return render(request, 'python/python_edit.html', {'form':form})
  


