from django import forms
from app.models import*
from django.contrib.auth.forms import AuthenticationForm, UsernameField ,PasswordResetForm, SetPasswordForm
from django.utils.translation import gettext, gettext_lazy as _
from ckeditor.widgets import CKEditorWidget
from django import forms
from django.urls import reverse
from django.contrib.auth import password_validation






class AboutForm(forms.ModelForm):
    class Meta:
        model = About
        fields = ['title', 'discriptions']

class AboutImageForm(forms.ModelForm):
    class Meta:
        model = AboutImage
        fields = ['image']

    def increase_num_files(self):
        self.fields['image'].max_num_files += 1
        return self

AboutImageFormSet = forms.inlineformset_factory(
    About,
    AboutImage,
    form=AboutImageForm,
    fields=['image'],
    can_delete=True,  # This will automatically add a DELETE checkbox
    extra=1,
)



# class CombinedAboutForm(forms.ModelForm):
#     image = forms.ImageField(required=False, widget=forms.ClearableFileInput(attrs={'class': 'clearablefileinput'}))

#     class Meta:
#         model = About
#         fields = ['title', 'discriptions']

#     def save(self, commit=True):
#         about = super().save(commit=commit)

#         if self.cleaned_data.get('image'):
#             AboutImage.objects.create(about=about, image=self.cleaned_data['image'])

#         return about

class BannerForm(forms.ModelForm):
    class Meta:
        model = BannarImage
        fields = '__all__'


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactDetails
        fields = '__all__'

class QueryForm(forms.ModelForm):
    class Meta:
        model = CustomerQuery
        fields = '__all__'


class Menu_categoriesForm(forms.ModelForm):
    class Meta:
        model = MenuCategories
        fields = '__all__'


class MenuForm(forms.ModelForm):
    short_discriptions = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Menu
        fields = '__all__'

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Services
        fields = '__all__'


class TestimonialsForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = '__all__'


class Why_UsForm(forms.ModelForm):
    class Meta:
        model = WhyChooseUs
        fields = '__all__'



class StaffLoginForm(AuthenticationForm):
    remember_me = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        help_text="Remember me",
    )

    username = forms.CharField(
        label="Username",
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )
    def init(self, *args, **kwargs):
        super().init(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['password'].widget.attrs.update({'class': 'form-control'})

    def get_context(self, request):
        context = super().get_context(request)
        context['forgot_password_url'] = reverse('app:password_reset')
        return context
    

class PasswordResetForm(PasswordResetForm):
    email = forms.EmailField(label=_("Email"), max_length=254, widget=forms.EmailInput(attrs={'autocomplete':'email', 'class':'form-control'}))


class SetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(label=_("New Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'new-password', 'class':'form-control'}), help_text=password_validation.password_validators_help_text_html())
    new_password2 = forms.CharField(label=_("Confirm Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'new-password','class':'form-control'}))
