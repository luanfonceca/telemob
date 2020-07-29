
from django.urls import path
from django.views.generic import TemplateView

from telemob.main import views


urlpatterns = [
    path('', views.HomeView.as_view(), name='index'),
    path(
        'intro-1/',
        TemplateView.as_view(template_name="onboarding-part-1.html"),
        name='onboarding-part-1'
    ),
    path(
        'intro-2/',
        TemplateView.as_view(template_name="onboarding-part-2.html"),
        name='onboarding-part-2'
    ),
    path(
        'intro-3/',
        TemplateView.as_view(template_name="onboarding-part-3.html"),
        name='onboarding-part-3'
    ),
    path('ufs/', views.ChooseState.as_view(), name='choose-state'),
    path(
        'ufs/<str:state>/politicos/',
        views.ChoosePolitician.as_view(),
        name='choose-politician'
    ),
    path(
        'ufs/<str:state>/politicos/<int:politician_id>/',
        views.ContactPolitician.as_view(),
        name='contact-politician'
    ),
    path(
        'ufs/<str:state>/politicos/<int:politician_id>/reportar/',
        views.ReportContact.as_view(),
        name='report-contact'
    ),
    path(
        'ufs/<str:state>/politicos/<int:politician_id>/reportado-com-sucesso/',
        views.ReportContactSuccess.as_view(),
        name='report-contact-success'
    ),
    path('sobre/', TemplateView.as_view(template_name="about.html"), name='about'),
]
