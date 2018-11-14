import re

from django import forms


class GameForm(forms.Form):
    number_of_players = forms.IntegerField(min_value=1, max_value=4)
    number_of_squares = forms.IntegerField(min_value=1, max_value=79)
    number_of_cards = forms.IntegerField(min_value=1, max_value=200)
    characters = forms.CharField()
    cards = forms.CharField()

    def clean(self):
        super(GameForm, self).clean()

        messages = {
            'characters': "Allowed format: AAAA",
            'cards': "Allowed format: A,AA,A"
        }

        characters = self.cleaned_data.get('characters')
        cards = self.cleaned_data.get('cards')

        if not re.match(r'[A-Z]', characters):
            self.add_error('characters', messages['characters'])

        if not re.match(r'[A-Z]+(?=[,])', cards):
            self.add_error('cards', messages['cards'])

        return self.cleaned_data
