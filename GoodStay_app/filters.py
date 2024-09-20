import django_filters
from django import forms
from django_filters import CharFilter

from GoodStay_app.models import Custom_warden


class WardenFilter(django_filters.FilterSet):
    name = CharFilter(field_name='name', label="", lookup_expr ='icontains', widget=forms.TextInput(attrs={
        'placeholder': 'Search Name', 'class': 'form-control'}))


    class Meta:
        model = Custom_warden
        fields = ('name',)