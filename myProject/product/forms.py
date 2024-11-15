
from django import forms
from product.models import Comment


class SearchForm(forms.Form):
    query = forms.CharField(max_length=100)

class CommentForm(forms.ModelForm):
    
    #ModelForm kullanıldığında, formun hangi modelle ilişkili olduğunu belirtmek için Meta sınıfındaki model alanı kullanılır.
    class Meta:
        model = Comment
        fields = ['subject','comment','rate']