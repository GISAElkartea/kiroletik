from django import forms

from autocomplete_light import ModelForm, ChoiceWidget

from .models import Team, TeamClassification, TeamResult


class TeamClassificationForm(ModelForm):
    team = forms.ModelChoiceField(
        required=True, queryset=Team.objects.all(),
        widget=ChoiceWidget('TeamAutocomplete'))

    class Meta:
        model = TeamClassification
        fields = ('team', 'season', 'points')


class TeamResultForm(ModelForm):
    team = forms.ModelChoiceField(
        required=True, queryset=Team.objects.all(),
        widget=ChoiceWidget('TeamAutocomplete'))

    class Meta:
        model = TeamResult
        fields = ('team', 'match', 'points')
