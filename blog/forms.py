from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    title   = forms.CharField(
                    widget=forms.TextInput(
                            attrs={
                                "placeholder": "Post Title...",
                            }
                        )
                    )
    content = forms.CharField(
                    widget=forms.Textarea(
                            attrs={
                                "placeholder": "",
                                "class": "fcontent",
                                "rows": 20,
                            }
                        )
                    )
    author  = forms.CharField(
                    required=False,
                    widget=forms.TextInput(
                            attrs={
                                "placeholder": "",
                            }
                        )
                    )

    class Meta:
        model = Post
        fields = [
            "title", 
            "content", 
            "author",
        ]
    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
#        if "kurwa" in title:
#            raise forms.ValidationError("This is not a valid title")
        return title

