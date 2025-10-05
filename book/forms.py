from django import forms


class CategoryForm(forms.Form):
    name = forms.CharField(
        max_length=50,
        label="عنوان",
        widget=forms.TextInput(
            attrs={
                "class": "form-control mt-2",
            }
        ),
    )
    description = forms.CharField(
        max_length=255,
        label="توضیحات",
        widget=forms.Textarea(attrs={"class": "form-control mt-2"}),
    )

    def clean_name(self):
        name = self.cleaned_data.get("name")
        if len(name) < 5:
            forms.ValidationError("این فیلد نمی تواند کمتر از ۵ کاراکتر داشته باشد")
        return name
