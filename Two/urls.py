from django.urls import path

from Two import views

urlpatterns = {
    path('getuser/', views.get_user),
    path('getusers/', views.get_users),
    path('getorders/', views.get_orders),
    path('getgrades/', views.get_grades),
    path('getcosts/', views.get_costs),
    path('getcompany/', views.get_company),
    path('getanimals/', views.get_animals),

}