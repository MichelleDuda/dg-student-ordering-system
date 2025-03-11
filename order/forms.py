from django import forms
from django.forms import inlineformset_factory
from .models import MenuWeek, Meal


class MenuWeekForm(forms.ModelForm):
    start_date = forms.DateField(
        widget=forms.DateInput(attrs={"type": "date", "class": "form-control"})
    )

    class Meta:
        model = MenuWeek
        fields = ['start_date']


class MealForm(forms.ModelForm):
    class Meta:
        model = Meal
        fields = [
            "day_of_week",
            "category",
            "name",
            "is_plant_based",
            "description",
        ]


MealFormSet = inlineformset_factory(
    MenuWeek, Meal, form=MealForm,
    extra=1,
    max_num=50,
    can_delete=True
)
MealFormSet.empty_permitted = True
