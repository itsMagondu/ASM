from django.forms import ModelForm
from photo.models import Photo

class PhotoForm(ModelForm):
    class Meta:
        model = Article
        fields = ['name', 'file', 'description','price','category','format','approved']
        
