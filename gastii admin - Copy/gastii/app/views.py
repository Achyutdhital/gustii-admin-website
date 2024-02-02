from django.shortcuts import render , redirect,get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView ,DetailView,FormView
from django.views import View
from .models import*
from .forms import*
from .models import About, AboutImage
from .forms import AboutForm, AboutImageForm
from django.forms import modelformset_factory ,inlineformset_factory

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import login , logout
from django.utils.decorators import method_decorator
from .decorators import superadmin_required
from django.views.generic import TemplateView





# Create your views here.
@method_decorator([login_required(login_url='login'), superadmin_required], name='dispatch')
class DashboardView(TemplateView):
    template_name = 'app/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context


@method_decorator([login_required(login_url='login'), superadmin_required], name='dispatch')
class BannarImageDetailView(View):
    def get(self, request, pk):
        banner_image = BannarImage.objects.get(pk=pk)
        form = BannerForm(instance=banner_image)
        context = {'banner_image': banner_image, 'form': form, 'edit_mode': False}
        return render(request,'app/banner_detail.html', context)

        
    

@method_decorator([login_required(login_url='login'), superadmin_required], name='dispatch')
class BannarImageEditView(View):
    def get(self, request, pk):
        banner_image = BannarImage.objects.get(pk=pk)
        form = BannerForm(instance=banner_image)
        context = {'banner_image': banner_image, 'form': form, 'edit_mode': True}
        return render(request, 'app/banner_edit.html', context)

    def post(self, request, pk):
        banner_image = BannarImage.objects.get(pk=pk)
        form = BannerForm(request.POST, request.FILES, instance=banner_image) 
        if form.is_valid():
            instance = form.save(commit=False)

            new_image = form.cleaned_data.get('banner_image')  
            if new_image is not None:
                instance.image.save(new_image.name, new_image, save=False)

            instance.save()

            return redirect('banner-detail', pk=pk)
        context = {'banner_image': banner_image, 'form': form, 'edit_mode': True}
        return render(request, 'app/banner_edit.html', context)


@method_decorator([login_required(login_url='login'), superadmin_required], name='dispatch')
class AboutDetailView(View):
    def get(self, request, pk):
        about = About.objects.get(pk=pk)
        context = {'about': about}
        return render(request, 'app/about_detail.html', context)
    

    
@method_decorator([login_required(login_url='login'), superadmin_required], name='dispatch')
class AboutEditView(View):
    def get(self, request, pk):
        about = About.objects.get(pk=pk)
        form = AboutForm(instance=about)
        image_formset = AboutImageFormSet(instance=about)
        context = {'about': about, 'form': form, 'image_formset': image_formset}
        return render(request, 'app/about_edit.html', context)

    def post(self, request, pk):
        about = About.objects.get(pk=pk)
        about_form = AboutForm(request.POST, instance=about)
        ImageFormSet = inlineformset_factory(
            About,
            AboutImage,
            form=AboutImageForm,
            fields=['image'],
            can_delete=True,
            extra=0  # Set to 0 to initially display existing images only
        )
        image_formset = ImageFormSet(request.POST, request.FILES, instance=about)

        if about_form.is_valid() and image_formset.is_valid():
            about_form.save()  # Update title and description

            for form in image_formset:
                if form.cleaned_data.get('DELETE'):
                    # Delete images marked for deletion
                    AboutImage.objects.get(id=form.instance.id).delete()
                elif form.cleaned_data.get('image'):
                    # Update or add new images
                    image = form.save(commit=False)
                    image.about = about
                    image.save()

            return redirect('about-detail', pk=about.pk)

        context = {
            'about': about,
            'about_form': about_form,
            'image_formset': image_formset,
        }
        return render(request, 'app/about_edit.html', context)
    
@method_decorator([login_required(login_url='login'), superadmin_required], name='dispatch')
class ContactDetailview(View):
    def get(self, request, pk):
        contact_details = ContactDetails.objects.get(pk=pk)
        context = {'contact_details': contact_details}
        return render(request, 'app/contact_details.html', context)
    
class ContactEditView(View):
    def get(self, request, pk):
        contact_details = ContactDetails.objects.get(pk=pk)
        form = ContactForm(instance=contact_details)
        context = {'contact_details': contact_details, 'form': form}
        return render(request, 'app/contact_edit.html', context)

    def post(self, request, pk):
        contact_details = ContactDetails.objects.get(pk=pk)
        form = ContactForm(request.POST, instance=contact_details)
        
        if form.is_valid():
            form.save()
            return redirect('contact-detail', pk=pk)
        
        context = {'contact_details': contact_details, 'form': form}
        return render(request, 'app/contact_edit.html', context)

@method_decorator([login_required(login_url='login'), superadmin_required], name='dispatch')    
class CustomerQueryListView(View):
    def get(self, request):
        customer_queries = CustomerQuery.objects.all()
        context = {'customer_queries': customer_queries}
        return render(request, 'app/customer_query_list.html', context)

@method_decorator([login_required(login_url='login'), superadmin_required], name='dispatch')   
class CustomerQueryDetailView(View):
    def get(self, request, pk):
        customer_query = get_object_or_404(CustomerQuery, pk=pk)
        context = {'customer_query': customer_query}
        return render(request, 'app/customer_query_detail.html', context)

@method_decorator([login_required(login_url='login'), superadmin_required], name='dispatch')   
class MenuCategoryListView(View):
    def get(self, request):
        menu_categories = MenuCategories.objects.all()
        context = {'menu_categories': menu_categories}
        return render(request, 'app/menu_category_list.html', context)
    
@method_decorator([login_required(login_url='login'), superadmin_required], name='dispatch')
class MenuCategoryAddEditView(View):
    def get(self, request, category_slug=None):
        if category_slug:
            category = get_object_or_404(MenuCategories, ctg_slug=category_slug)
            form = Menu_categoriesForm(instance=category)
        else:
            form = Menu_categoriesForm()

        return render(request, 'app/menu_category_edit.html', {'form': form})

    def post(self, request, category_slug=None):
        if category_slug:
            category = get_object_or_404(MenuCategories, ctg_slug=category_slug)
            form = Menu_categoriesForm(request.POST, request.FILES, instance=category)
        else:
            form = Menu_categoriesForm(request.POST, request.FILES)

        if form.is_valid():
            instance = form.save(commit=False)

            new_image = form.cleaned_data.get('category')
            if new_image:
                instance.category.save(new_image.name, new_image, save=False)

            instance.save()
            return redirect('menu-category-list')

        return render(request, 'app/menu_category_edit.html', {'form': form})

@method_decorator([login_required(login_url='login'), superadmin_required], name='dispatch')   
class MenuCategoryDeleteView(View):
    def get(self, request, category_slug):
        category = get_object_or_404(MenuCategories, ctg_slug=category_slug)
        return render(request, 'app/menu_category_delete_confirm.html', {'category': category})

    def post(self, request, category_slug):
        category = get_object_or_404(MenuCategories, ctg_slug=category_slug)
        category.delete()
        return redirect('menu-category-list')

@method_decorator([login_required(login_url='login'), superadmin_required], name='dispatch')   
class MenuListView(View):
    def get(self, request):
        menus = Menu.objects.all()
        context = {'menus': menus}
        return render(request, 'app/menu_list.html', context)
    
@method_decorator([login_required(login_url='login'), superadmin_required], name='dispatch')
class MenuAddEditView(View):
    def get(self, request, item_slug=None):
        if item_slug:
            menu_item = get_object_or_404(Menu, item_slug=item_slug)
            form = MenuForm(instance=menu_item)
        else:
            form = MenuForm()

        return render(request, 'app/menu_edit.html', {'form': form})

    def post(self, request, item_slug=None):
        if item_slug:
            menu_item = get_object_or_404(Menu, item_slug=item_slug)
            form = MenuForm(request.POST, request.FILES, instance=menu_item)
        else:
            form = MenuForm(request.POST, request.FILES)

        if form.is_valid():
            instance = form.save(commit=False)
            new_image = form.cleaned_data.get('menu_item')
            if new_image:
                instance.menu_item.save(new_image.name, new_image, save=False)
            instance.save()
            return redirect('menu-list')

        return render(request, 'app/menu_edit.html', {'form': form})
    
@method_decorator([login_required(login_url='login'), superadmin_required], name='dispatch')
class MenuDeleteView(View):
    def get(self, request, item_slug):
        menu_item = get_object_or_404(Menu, item_slug=item_slug)
        return render(request, 'app/menu_delete_confirm.html', {'menu': menu_item})

    def post(self, request, item_slug):
        menu_item = get_object_or_404(Menu, item_slug=item_slug)
        menu_item.delete()
        return redirect('menu-list')

@method_decorator([login_required(login_url='login'), superadmin_required], name='dispatch')
class ServiceListView(View):

    def get(self, request):
        services = Services.objects.all()
        context = {'services': services}
        return render(request, 'app/service_list.html', context)

@method_decorator([login_required(login_url='login'), superadmin_required], name='dispatch')    
class ServiceAddEditView(View):
    template_name = 'app/service_add_edit.html'

    def get(self, request, pk=None):
        if pk:
            service = get_object_or_404(Services, pk=pk)
            form = ServiceForm(instance=service)
        else:
            form = ServiceForm()
        context = {'form': form}
        return render(request, 'app/service_add_edit.html', context)

    def post(self, request, pk=None):
        if pk:
            service = get_object_or_404(Services, pk=pk)
            form = ServiceForm(request.POST, request.FILES, instance=service)
        else:
            form = ServiceForm(request.POST, request.FILES)
        
        if form.is_valid():
            instance = form.save(commit=False)
            new_image = form.cleaned_data.get('service')
            if new_image:
                instance.service.save(new_image.name, new_image, save=False)
            instance.save()
            return redirect('service-list')
        
        context = {'form': form}
        return render(request, 'app/service_add_edit.html', context)

@method_decorator([login_required(login_url='login'), superadmin_required], name='dispatch')   
class ServiceDeleteView(View):

    def get(self, request, pk):
        service = get_object_or_404(Services, pk=pk)
        return render(request, 'app/service_delete.html', {'service': service})

    def post(self, request, pk):
        service = get_object_or_404(Services, pk=pk)
        service.delete()
        return redirect('service-list')

@method_decorator([login_required(login_url='login'), superadmin_required], name='dispatch')    
class TestimonialListView(View):
    def get(self, request):
        testimonials = Testimonial.objects.all()
        context = {'testimonials': testimonials}
        return render(request, 'app/testimonial_list.html', context)

@method_decorator([login_required(login_url='login'), superadmin_required], name='dispatch')
class TestimonialAddEditView(View):
    def get(self, request, testimonial_id=None):
        if testimonial_id:
            testimonial = get_object_or_404(Testimonial, id=testimonial_id)
            form = TestimonialsForm(instance=testimonial)
        else:
            form = TestimonialsForm()
        return render(request, 'app/testimonial_add_edit.html', {'form': form})

    def post(self, request, testimonial_id=None):
        if testimonial_id:
            testimonial = get_object_or_404(Testimonial, id=testimonial_id)
            form = TestimonialsForm(request.POST, request.FILES, instance=testimonial)
        else:
            form = TestimonialsForm(request.POST, request.FILES)

        if form.is_valid():
            instance = form.save(commit=False)
            new_image = form.cleaned_data.get('testimonial')
            if new_image:
                instance.testimonial.save(new_image.name, new_image, save=False)
            instance.save()
            return redirect('testimonial-list')

        return render(request, 'app/testimonial_add_edit.html', {'form': form})

@method_decorator([login_required(login_url='login'), superadmin_required], name='dispatch')   
class TestimonialDeleteView(View):
    def get(self, request, testimonial_id):
        testimonial = get_object_or_404(Testimonial, id=testimonial_id)
        return render(request, 'app/testimonial_delete.html', {'testimonial': testimonial})

    def post(self, request, testimonial_id):
        testimonial = get_object_or_404(Testimonial, id=testimonial_id)
        testimonial.delete()
        return redirect('testimonial-list')

@method_decorator([login_required(login_url='login'), superadmin_required], name='dispatch')   
class WhyChooseUsDetailView(View):
    def get(self, request, pk):
        why_us = get_object_or_404(WhyChooseUs, pk=pk)
        context = {'why_us': why_us, 'edit_mode': False}
        return render(request, 'app/why_us_detail.html', context)

@method_decorator([login_required(login_url='login'), superadmin_required], name='dispatch')    
class WhyChooseUsEditView(View):
    def get(self, request, pk):
        why_us = get_object_or_404(WhyChooseUs, pk=pk)
        form = Why_UsForm(instance=why_us)
        context = {'why_us': why_us, 'form': form, 'edit_mode': True}
        return render(request, 'app/why_us_edit.html', context)

    def post(self, request, pk):
        why_us = get_object_or_404(WhyChooseUs, pk=pk)
        form = Why_UsForm(request.POST, instance=why_us)

        if form.is_valid():
            form.save()
            return redirect('why_us-detail', pk=pk)

        context = {'why_us': why_us, 'form': form, 'edit_mode': True}
        return render(request, 'app/why_us_edit.html', context)
    
def login_view(request):
    if request.method == 'POST':
        form = StaffLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if not user.is_superuser:
                messages.warning(request, "You do not have superuser privileges.")
                return redirect('login')
            return redirect('index')  
        else:
            messages.warning(request, "Invalid username or password!")
    else:
        form = StaffLoginForm()

    return render(request, 'app/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')









def error_400_view(request, not_found):
    return render(request, 'app/pages-404.html', status=400)