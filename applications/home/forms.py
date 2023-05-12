# from django import forms

# from .models import Suscriber, Contact


# class SuscribersForm(forms.ModelForm):
#     class Meta:
#         model= Suscriber

#         fields= ('email',)
#         widgets= { 
#             'email': forms.EmailInput(
#                 attrs= {
#                     'placeholder': 'Email',
#                 }
#             )
#         }

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         for field in iter(self.fields):
#             self.fields[field].widget.attrs.update({
#                 'class': 'form-control'
#             })


# class ContactForm(forms.ModelForm):
#     class Meta:
#         model= Contact

#         fields= ('__all__')

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         for field in iter(self.fields):
#             self.fields[field].widget.attrs.update({
#                 'class': 'form-control'
#             })
