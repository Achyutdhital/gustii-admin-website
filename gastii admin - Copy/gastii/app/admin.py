from django.contrib import admin
from . models import BannarImage, About, AboutImage, MenuCategories,WhyChooseUs, Menu,Testimonial,Services,ContactDetails,CustomerQuery




admin.site.site_header = 'Gastii Admin Panel'        
admin.site.index_title = 'Gastii'                
admin.site.site_title = 'Welcome to Gastii admin panel' 




class BannarImageAdmin(admin.ModelAdmin):
    model = BannarImage
    list_display =['id','title','image']

    def has_add_permission(self, request, obj=None):
        return False
    
    def has_delete_permission(self, request, obj=None):
        return False
    
    def render_change_form(self, request, context, add=False, change=False, form_url='', obj=None):
        context.update({
            'show_save': True,
            'show_save_and_continue': False,
            'show_save_and_add_another': False,
            'show_delete': False
        })
        return super().render_change_form(request, context, add, change, form_url, obj)
    
admin.site.register(BannarImage, BannarImageAdmin)

class AboutImageAdmin(admin.TabularInline):
    model = AboutImage

class AboutAdmin(admin.ModelAdmin):
    inlines = [AboutImageAdmin]
    list_display = ['title']

    def has_add_permission(self, request, obj=None):
        return False
    
    def has_delete_permission(self, request, obj=None):
        return False
    
    def render_change_form(self, request, context, add=False, change=False, form_url='', obj=None):
        context.update({
            'show_save': True,
            'show_save_and_continue': False,
            'show_save_and_add_another': False,
            'show_delete': False
        })
        return super().render_change_form(request, context, add, change, form_url, obj)
    
admin.site.register(About,AboutAdmin)



class MenuCategoriesAdmin(admin.ModelAdmin):
    model = MenuCategories
    list_display = ['categori_name','icon']
admin.site.register(MenuCategories, MenuCategoriesAdmin)

class MenuAdmin(admin.ModelAdmin):
    model = Menu
    list_display = ['name','price','image','categori']
admin.site.register(Menu, MenuAdmin)


class TestimonialAdmin(admin.ModelAdmin):
    model = Testimonial
    list_display =['name','image']
admin.site.register(Testimonial, TestimonialAdmin)


class ServicesAdmin(admin.ModelAdmin):
    model = Services
    list_display = ['service_name','icon']
admin.site.register(Services,ServicesAdmin)



class ContactDetailsAdmin(admin.ModelAdmin):
    model  = ContactDetails
    list_display = ['location','phoneNo','email']

    def has_add_permission(self, request, obj=None):
        return False
    
    def has_delete_permission(self, request, obj=None):
        return False
    
    def render_change_form(self, request, context, add=False, change=False, form_url='', obj=None):
        context.update({
            'show_save': True,
            'show_save_and_continue': False,
            'show_save_and_add_another': False,
            'show_delete': False
        })
        return super().render_change_form(request, context, add, change, form_url, obj)
    
admin.site.register(ContactDetails,ContactDetailsAdmin)

class CustomerQueryAdmin(admin.ModelAdmin):
    model:CustomerQuery
    list_display =['fullname','email']

    def has_add_permission(self, request, obj=None):
        return False
    
    def has_delete_permission(self, request, obj=None):
        return False
    
    def render_change_form(self, request, context, add=False, change=False, form_url='', obj=None):
        context.update({
            'show_save': True,
            'show_save_and_continue': False,
            'show_save_and_add_another': False,
            'show_delete': True
        })
        return super().render_change_form(request, context, add, change, form_url, obj)
    
admin.site.register(CustomerQuery, CustomerQueryAdmin)

class WhyChooseUsAdmin(admin.ModelAdmin):
    model = WhyChooseUs
    list_display= ['videoTitle','videoUrl']

    def has_add_permission(self, request, obj=None):
        return False
    
    def has_delete_permission(self, request, obj=None):
        return False
    
    def render_change_form(self, request, context, add=False, change=False, form_url='', obj=None):
        context.update({
            'show_save': True,
            'show_save_and_continue': False,
            'show_save_and_add_another': False,
            'show_delete': False
        })
        return super().render_change_form(request, context, add, change, form_url, obj)
    
admin.site.register(WhyChooseUs,WhyChooseUsAdmin)