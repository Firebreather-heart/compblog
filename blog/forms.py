from django import forms 
from tinymce.widgets import TinyMCE
from .models import Post

class TinyMceWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False 

class PostForm(forms.ModelForm):
    content = forms.CharField(widget=TinyMceWidget(
        attrs = {'required':False, 'cols':30, 'rows':30}
    ))
    widget = {
        'id':forms.UUIDField()
    }
    
    class Meta:
        model = Post 
        fields = ('content' , 'img', 'status', 'title', )

class SearchForm(forms.Form):
    query = forms.CharField
