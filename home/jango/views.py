from django.shortcuts import render
from django.utils import timezone
from .models import Jango
from django.shortcuts import render, redirect, get_object_or_404
from .forms import JangoForm
from django.views import View


# Create your views here.
"""class Jango(View):
  def get(self, request, *args, **kwargs):
    return render(request, 'jango/base.html')"""
    
def jango_list(request):
    jangos = Jango.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'jango/jango_list.html', {'jangos':jangos})
  
def jango_detail(request, pk):
      jango = get_object_or_404(Jango, pk=pk)
      return render(request, 'jango/jango_detail.html', {'jango': jango})
  
def jango_new(request):
      if request.method == "JANGO":
          form = JangoForm(request.JANGO)
          if form.is_valid():
              jango = form.save(commit=False)
              jango.author = request.user
              jango.published_date = timezone.now()
              jango.save()
              return redirect('jango_detail', pk=jango.pk)
      else:
          form = JangoForm()
      return render(request, 'jango/jango_edit.html', {'form': form})
    
def jango_edit(request, pk):
      jango = get_object_or_404(Jango, pk=pk)
      if request.method == "JANGO":
        form = JangoForm(request.JANGO, instance=jango)
        if form.is_valid():
          jango = form.save(commit=False)
          jango.author = request.user
          jango.published_date = timezone.now()
          jango.save()
      else:
        form = JangoForm(instance=jango)
      return render(request, 'jango/jango_edit.html', {'form':form})


