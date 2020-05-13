from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect
from django.views import View
from .forms import taskForm
from .models import tasks
# Create your views here.
class tasksList(View):
    
    template_name = 'todolist/todo.html'
    def get(self,request):
        t = tasks.objects.all()
        return render(request,self.template_name,{'tasks':t})

todoList = tasksList.as_view()

class addTask(View):
    def post(self,request):
        form = taskForm(request.POST)
        if form.is_valid():
            t = tasks(title = request.POST['task'],description = request.POST['description'], deadline = request.POST['deadline'])
            t.save()
        return HttpResponseRedirect('/')
    def get(self, request):
        return HttpResponseRedirect('/')

addTask = addTask.as_view()

class complete(View):
    def get(self,request,identity):
        print(identity)
        t = get_object_or_404(tasks,identity = identity)
        t.complete = 'Y'
        t.save()
        return HttpResponseRedirect('/')

complete = complete.as_view()


class delete(View):
    def get(self,request,identity):
        t=get_object_or_404(tasks,identity = identity)
        t.delete()
        return HttpResponseRedirect('/')

delete = delete.as_view()