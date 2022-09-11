from django.shortcuts import render
from django.utils import timezone
from .models import Sidebar
from django.shortcuts import render, redirect, get_object_or_404
from .forms import SidebarForm
from django.views import View


# Create your views here.
"""class Sidebar(View):
  def get(self, request, *args, **kwargs):
    return render(request, 'sidebar/base.html')"""
    
def sidebar_list(request):
    sidebars = Sidebar.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'sidebar/sidebar_list.html', {'sidebars':sidebars})
  
def sidebar_detail(request, pk):
      sidebar = get_object_or_404(Sidebar, pk=pk)
      return render(request, 'sidebar/sidebar_detail.html', {'sidebar': sidebar})
  
def sidebar_new(request):
      if request.method == "SIDEBAR":
          form = SidebarForm(request.SIDEBAR)
          if form.is_valid():
              sidebar = form.save(commit=False)
              sidebar.author = request.user
              sidebar.published_date = timezone.now()
              sidebar.save()
              return redirect('sidebar_detail', pk=sidebar.pk)
      else:
          form = SidebarForm()
      return render(request, 'sidebar/sidebar_edit.html', {'form': form})
  
def sidebar_edit(request, pk):
    sidebar = get_object_or_404(Sidebar, pk=pk)
    if request.method == "SIDEBAR":
      form = SidebarForm(request.SIDEBAR, instance=sidebar)
      if form.is_valid():
        sidebar = form.save(commit=False)
        sidebar.author = request.user
        sidebar.published_date = timezone.now()
        sidebar.save()
    else:
      form = SidebarForm(instance=sidebar)
    return render(request, 'sidebar/sidebar_edit.html', {'form':form})
