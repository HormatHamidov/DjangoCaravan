from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    timestamp = forms.CharField(widget= forms.DateInput(attrs= {"type": "date"}))
    class Meta:
        model = Article
        fields = '__all__'
        # exlude = ('author') Olmamasini istediyin fieldin secimi
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({"class":"form-control"})
    # init metodundan istifade ederek butun fieldlerimi bootsrapdan istifade ederek daha duzgun gozel hala saliram
        
        
    def clean(self):
        print(self.cleaned_data)
        return super().clean()