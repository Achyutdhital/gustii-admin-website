from django.urls import path, include, reverse_lazy
from .import views
from .views import*
from django.contrib.auth import views as auth_views
from .forms import  PasswordResetForm, SetPasswordForm


urlpatterns = [
    path('',views.DashboardView.as_view(), name='index'),

    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    path('password-reset/',auth_views.PasswordResetView.as_view(template_name='app/password_reset.html',form_class=PasswordResetForm,success_url='/password-reset-done/'),name="password-reset"),
    path('password-reset-done/',auth_views.PasswordResetDoneView.as_view(template_name='app/password_reset_done.html'),name="password-reset-done"),
    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name="password_reset_confirm"),
    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name='app/password_reset_complete.html'),name="password-reset-complete"),

    path('password-change/', auth_views.PasswordChangeView.as_view(template_name='app/change_password.html',form_class=PasswordChangeForm, success_url='/password-change-done/'), name="password-change"),
    path('password-change-done/', auth_views.PasswordChangeDoneView.as_view(template_name='app/password_change_done.html'), name="password-change-done"),

    path('banner/<int:pk>/', BannarImageDetailView.as_view(), name='banner-detail'),
    path('banner/<int:pk>/edit/', BannarImageEditView.as_view(), name='banner-edit'),
    path('about/<int:pk>/', views.AboutDetailView.as_view(), name='about-detail'),
    path('about/<int:pk>/edit/', views.AboutEditView.as_view(), name='about-edit'),
    path('contact/<int:pk>/', views.ContactDetailview.as_view(), name='contact-detail'),
    path('contact/<int:pk>/edit/', views.ContactEditView.as_view(), name='contact-edit'),
    path('customer-queries/', CustomerQueryListView.as_view(), name='customer-query-list'),
    path('customer-query/<int:pk>/edit/', CustomerQueryDetailView.as_view(), name='customer-query-detail'),
    path('menu-categories/', MenuCategoryListView.as_view(), name='menu-category-list'),
    path('menu-category/add/', MenuCategoryAddEditView.as_view(), name='menu-category-add'),
    path('menu-category/edit/<slug:category_slug>/', MenuCategoryAddEditView.as_view(), name='menu-category-edit'),
    path('menu-category/delete/<slug:category_slug>/', MenuCategoryDeleteView.as_view(), name='menu-category-delete'),
    path('menu-list/', MenuListView.as_view(), name='menu-list'),
    path('menu/add/', views.MenuAddEditView.as_view(), name='menu-add'),
    path('menu/edit/<str:item_slug>/', views.MenuAddEditView.as_view(), name='menu-edit'),
    path('menu/delete/<str:item_slug>/', views.MenuDeleteView.as_view(), name='menu-delete'),
    path('services/', ServiceListView.as_view(), name='service-list'),
    path('services/add/', ServiceAddEditView.as_view(), name='service-add'),
    path('services/edit/<int:pk>/', ServiceAddEditView.as_view(), name='service-edit'),
    path('services/delete/<int:pk>/', ServiceDeleteView.as_view(), name='service-delete'),
    path('testimonials/', TestimonialListView.as_view(), name='testimonial-list'),
    path('testimonials/add/', TestimonialAddEditView.as_view(), name='testimonial-add'),
    path('testimonials/edit/<int:testimonial_id>/', TestimonialAddEditView.as_view(), name='testimonial-edit'),
    path('testimonials/delete/<int:testimonial_id>/', TestimonialDeleteView.as_view(), name='testimonial-delete'),
    path('why-us/<int:pk>/', views.WhyChooseUsDetailView.as_view(), name='why_us-detail'),
    path('why-us/<int:pk>/edit/', views.WhyChooseUsEditView.as_view(), name='why_us-edit'),

    # path('<path:not_found>', error_400_view, name='catch_all_404'),
]
handler400 = views.error_400_view
