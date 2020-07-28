
from django.urls import path
from django.views.generic import TemplateView

from telemob.main.views import index, politician_list, report_contact


urlpatterns = [
    path('', index, name='index'),
    path(
        'onboarding/part-1/',
        TemplateView.as_view(template_name="onboarding-part-1.html"),
        name='onboarding-part-1'
    ),
    path(
        'onboarding/part-2/',
        TemplateView.as_view(template_name="onboarding-part-2.html"),
        name='onboarding-part-2'
    ),
    path(
        'onboarding/part-3/',
        TemplateView.as_view(template_name="onboarding-part-3.html"),
        name='onboarding-part-3'
    ),
    path(
        'choose/state/',
        TemplateView.as_view(template_name="choose-state.html"),
        name='choose-state'
    ),
    path(
        'choose/politician/',
        TemplateView.as_view(template_name="choose-politician.html"),
        name='choose-politician'
    ),
    path(
        'contact/politician/',
        TemplateView.as_view(template_name="contact-politician.html"),
        name='contact-politician'
    ),
    path(
        'report/contact/',
        TemplateView.as_view(template_name="report-contact.html"),
        name='report-contact'
    ),
    path(
        'report/contact/success/',
        TemplateView.as_view(template_name="report-contact-success.html"),
        name='report-contact-success'
    ),
    # path('politicos/<int:campaign_id>/', politician_list, name='state_list'),
    # path('politicos/<int:campaign_id>/<str:uf>/', politician_list, name='politician_list'),
    # path('contato/<int:campaign_id>/<int:politician_id>/', report_contact, name='report_contact'),
    path('sobre/', TemplateView.as_view(template_name="about.html"), name='about'),
]
