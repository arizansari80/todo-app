from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .models import Todo, Priority
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

class IndexView(generic.ListView):
    template_name = 'todos/index.html'
    # context_object_name = 'todo_list'
    # extra_context= {'priorities': [(item.value, item.name) for item in Priority]}

    def get_queryset(self):
        """Return all the latest todos."""
        return Todo.objects.order_by('isCompleted', 'priority', '-created_at')

    def get_context_data(self,*args, **kwargs):
        context = super(IndexView, self).get_context_data(*args,**kwargs)
        context['todo_list'] = Todo.objects.order_by('isCompleted', 'priority', '-created_at')
        context['priorities'] = [{'value': item.value, 'name': item.name} for item in Priority]
        return context

@csrf_exempt
def add(request):
    title = request.POST['title']
    priority = request.POST['priority']
    Todo.objects.create(title=title, priority=priority)

    return redirect('todos:index')

@csrf_exempt
def delete(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    todo.delete()

    return redirect('todos:index')

@csrf_exempt
def update(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    isCompleted = request.POST.get('isCompleted', False)
    if isCompleted == 'on':
        isCompleted = True
    
    todo.isCompleted = isCompleted

    todo.save()
    return redirect('todos:index')