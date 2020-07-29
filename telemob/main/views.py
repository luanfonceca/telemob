
from django.db.models import Count, Sum
from django.views.generic import (
    FormView, TemplateView, DetailView,
    CreateView,
)
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import StateForm
from .models import Campaign, Politician, Contact


class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        campaign = Campaign.objects.first()
        context.update(
            campaign=campaign,
            contacts=campaign.contact_set.count(),
        )
        return context


class ChooseState(FormView):
    template_name = 'choose-state.html'
    form_class = StateForm

    def form_valid(self, form):
        data = form.cleaned_data
        return HttpResponseRedirect(
            reverse('choose-politician', args=(data['state'],))
        )


class ChoosePolitician(TemplateView):
    template_name = 'choose-politician.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        state = kwargs.get('state')
        if state:
            politician_list = Politician.objects.filter(uf__iexact=state)

        politician_list = politician_list.annotate(
            contacts=Count('contact')
        ).order_by('contacts', 'parliamentary_name')
        total_contacts = politician_list.aggregate(total=Sum('contacts'))['total']

        context.update(
            politician_list=politician_list,
            total_contacts=total_contacts,
        )
        return context


class ContactPolitician(DetailView):
    queryset = Politician.objects.annotate(contacts=Count('contact'))
    pk_url_kwarg = 'politician_id'
    template_name = 'contact-politician.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            state=self.kwargs.get('state'),
            campaign=Campaign.objects.first(),
        )
        return context


class ReportContact(CreateView):
    model = Contact
    fields = ['contacted_by', 'result']
    template_name = 'report-contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        state = self.kwargs.get('state')
        politician_id = self.kwargs.get('politician_id')

        context.update(
            state=state,
            politician=Politician.objects.get(pk=politician_id, uf=state),
        )
        return context

    def form_valid(self, form):
        state = self.kwargs.get('state')
        politician_id = self.kwargs.get('politician_id')

        self.contact = form.save(commit=False)
        self.contact.campaign = Campaign.objects.first()
        self.contact.politician = Politician.objects.get(pk=politician_id, uf=state)
        self.contact.save()

        return HttpResponseRedirect(
            reverse('report-contact-success', args=(state, politician_id))
        )


class ReportContactSuccess(TemplateView):
    template_name = 'report-contact-success.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        campaign = Campaign.objects.first()
        total_contacts = campaign.contact_set.count()

        context.update(
            total_contacts=total_contacts,
        )
        return context
