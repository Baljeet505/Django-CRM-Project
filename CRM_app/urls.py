from django.urls import path
from CRM_app import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.Login, name='login'),
    path('logout/', views.Logout, name='logout'),
    path('Register/', views.Register_user, name='Register'),
    path('Record/<int:pk>', views.customer_record, name='Record'),
    path('delete_record/<int:pk>', views.delete_record, name='delete'),
    path('add_record/', views.add_record, name='add_record'),
    path('update_record/<int:pk>', views.update_record, name='update'),
    path('password_reset' , auth_views.PasswordResetView.as_view(template_name="CRM_app/password_reset.html"), name="password_reset"),
    path('password_reset_done' , auth_views.PasswordResetDoneView.as_view(template_name="CRM_app/password_reset_done.html"), name="password_reset_done"),
    path('password_reset_confirm/<uidb64>/<token>/' , auth_views.PasswordResetConfirmView.as_view(template_name="CRM_app/password_reset_confirm.html"), name="password_reset_confirm"),
    path('password_reset_complete' , auth_views.PasswordResetCompleteView.as_view(template_name="CRM_app/password_reset_complete.html"), name="password_reset_complete")
]
