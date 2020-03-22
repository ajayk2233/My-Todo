from django.shortcuts import render,redirect,HttpResponseRedirect
from .models import TodoModel,TodoModelForm
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.urls import reverse_lazy
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

@login_required(login_url='/auth1/signin')
def show(request,id=None,search=None):
    if search is not None:
        search = request.GET.get('search')
        search = search.strip()
        if search:
            object_list = TodoModel.objects.order_by('-id').filter(Q(name__contains=search) | Q(data__contains=search),user=request.user)
        else:
            object_list = TodoModel.objects.order_by('-id').filter(user=request.user)
        return render(request, 'show.html',{'object_list':object_list,'search':search})
    if id is not None:
        object_list = TodoModel.objects.get(id=id)
        if object_list.status == False:
            object_list.status = True
        else:
            object_list.status = False
        object_list.save()    
        return redirect('/')
    else:
        session_export = None
        try:
            request.session['message']
            session_export = request.session['message']
            del request.session['message']
        except:
            pass
        session_login_check = None
        try:
            request.session['login_check']
            session_login_check = request.session['login_check']
            del request.session['login_check']
        except:
            pass
        object_list = TodoModel.objects.filter(user=request.user)
        # Page Number
        paginator = Paginator(object_list,2)
        page = request.GET.get('page')
        try:
            object_list = paginator.page(page)
        except PageNotAnInteger:
            object_list = paginator.page(1)
        except EmptyPage:
            object_list = paginator.page(paginator.num_pages)
        return render(request,'show.html',{
            'object_list':object_list,
            'session_login_check':session_login_check,
            'session_export':session_export
            })

class Details(DetailView):
    model = TodoModel
    template_name = 'details.html'

class Create(CreateView):
    form_class = TodoModelForm
    template_name = 'create.html'
    success_url = '/'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class Update(UpdateView):
    form_class = TodoModelForm
    template_name = 'create.html'
    success_url = '/'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    def get_queryset(self):
        id = self.kwargs['pk']
        return TodoModel.objects.filter(pk=id)

class Delete(DeleteView):
    model = TodoModel
    success_url = ('/')

# Export Todo List to text file
import os

def export(request):
    object_list = TodoModel.objects.filter(user=request.user)
    try:
        os.mkdir('C:\\My-Todo')
    except:
        pass
    with open('C:\\My-Todo\\My-Todo.txt','a') as f:
        f.write(f"---Hey {request.user} your data is Successfully Exported---\n\n")
        for i in object_list:
            f.write(i.name + '\n' + i.data + '\n\n')
    request.session['message'] = 'Successfully Exported to C:\\My-Todo'
    return HttpResponseRedirect('/')