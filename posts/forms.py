from django import forms
from posts.models import Post


class PostCrateForm(forms.Form):
    image = forms.ImageField()
    title = forms.CharField(max_length=255)
    content = forms.CharField(max_length=1000)
    rate = forms.IntegerField(min_value=0, max_value=10)

    def clean_post(self):
        clean_data = super().clean()
        title = clean_data.get("title")
        content = clean_data.get("content")
        if not title and not content:
            raise forms.ValidationError("Заполните все поля")
        if title == content:
            raise forms.ValidationError("Тайтл не должен быть равен контенту")
        return clean_data
    
class PostModelForm(forms.ModelForm):
    class Meta:
            model = Post
            fields = ["image", "title", "content", "rate"]