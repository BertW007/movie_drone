from django import forms

from footage.models import Footage, FootageDetail


class FootageForm(forms.ModelForm):
    link = forms.URLField(help_text='Insert a youtube link here.')
    description = forms.CharField(max_length=35, help_text="The max length of the description is 35 digits.")
    class Meta:
        model = Footage
        fields = ["link", "description"]


CITIES = [

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
        fields = ["about_me", "pricing", "video_type", "city"]

class FootageDetailEditForm(FootageDetailCreateForm):
    pass