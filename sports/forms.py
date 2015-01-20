from django import forms

from autocomplete_light import ModelForm, ChoiceWidget

from .models import Team, TeamClassification, TeamResult


class TeamClassificationForm(ModelForm):
    team = forms.ModelChoiceField(
        required=True, queryset=Team.objects.all(),
        widget=ChoiceWidget('TeamAutocomplete'))

    class Meta:
        model = TeamClassification
        fields = ('position', 'team', 'season', 'points')


class TeamResultForm(ModelForm):
    team = forms.ModelChoiceField(
        required=True, queryset=Team.objects.all(),
        widget=ChoiceWidget('TeamAutocomplete'))

    class Meta:
        model = TeamResult
        fields = ('position', 'team', 'match', 'points')
