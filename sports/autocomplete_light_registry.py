import autocomplete_light

from .models import Team


autocomplete_light.register(Team,
                            search_fields=['name'])
