from django import forms
from blog.models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model= Post
        fields = ('title','text')
    
    def save_form(self, request, instance, form, change):
        user = request.user 
        instance = form.save(commit=False)
        if not change or not instance.author:
            instance.author = user
        instance.modified_by = user
        instance.save()
        form.save_m2m()
        return instance
