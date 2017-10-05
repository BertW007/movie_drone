from django import forms

from footage.models import Footage, FootageDetail


class FootageForm(forms.ModelForm):
    link = forms.URLField(help_text='Youtube Link')
    description = forms.CharField(max_length=35, help_text="The max length - 35 digits")

    class Meta:
        model = Footage
        fields = ["link", "description"]


CITY = [

    ("Białystok"  ,"Białystok"  ),
    ("Bydgoszcz"  ,"Bydgoszcz"  ),
    ("Częstochowa","Częstochowa"),
    ("Gdynia"     ,"Gdynia"     ),
    ("Gdańsk"     ,"Gdańsk"     ),
    ("Łódź"       ,"Łódź"       ),
    ("Katowice"   ,"Katowice"   ),
    ("Kraków"     ,"Kraków"     ),
    ("Lublin"     ,"Lublin"     ),
    ("Opole"      ,"Opole"      ),
    ("Poznań"     ,"Poznań"     ),
    ("Radom"      ,"Radom"      ),
    ("Sosnowiec"  ,"Sosnowiec"  ),
    ("Szczecin"   ,"Szczecin"   ),
    ("Toruń"      ,"Toruń"      ),
    ("Warszawa"   ,"Warszawa"   ),
    ("Wrocław"    ,"Wrocław"    ),

]


class FootageDetailCreateForm(forms.ModelForm):
    class Meta:
        model = FootageDetail
        fields = ["about_me", "pricing", "video_type"]

    city = forms.MultipleChoiceField(choices=CITY)
class FootageDetailEditForm(FootageDetailCreateForm):
    pass

class UserSearchForm(forms.Form):
    city = forms.ChoiceField(choices=CITY)
    maximum_price = forms.IntegerField(initial=1000)