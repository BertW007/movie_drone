from django import forms

from footage.models import Footage, UserDetails


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


class UserDetailsForm(forms.ModelForm):
    class Meta:
        model = UserDetails
        fields = ["about_me", "pricing", "video_type", "cities"]

class EditDetailsForm(UserDetailsForm):
    pass