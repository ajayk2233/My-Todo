from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.urls import reverse,reverse_lazy

class TodoModel(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=30)
    date_created = models.DateField(auto_now_add=True)
    data = models.TextField()
    status = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('todo:details',kwargs={"pk":self.pk})

    class Meta:
        ordering = ['-date_created']

class TodoModelForm(forms.ModelForm):
    class Meta:
        model = TodoModel
        fields = ('user','name','data')
        
        widgets = {
            'name': forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Enter Title',
                'autofocus':'True',
                'tabindex':'1'
                }),
            'data': forms.Textarea(attrs={
                'class':'form-control',
                'rows':4,
                'placeholder':'Start Typing data',
                'tabindex':'2',
                })
            
        }