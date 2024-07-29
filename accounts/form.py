from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterCustomerForm(UserCreationForm):
    SECTOR_CHOICES = [
        ('', ''),
        ('Portaria', 'Portaria'),
        ('Manutenção', 'Manutenção'),
        ('T.I - Desenvolvimento', 'T.I - Desenvolvimento'),
        ('Pintura', 'Pintura'),
        ('Prototipos', 'Prototipos'),
        ('Compras', 'Compras'),
        ('Carpintaria', 'Carpintaria'),
        ('Qualidade', 'Qualidade'),
        ('Almoxarifado', 'Almoxarifado'),
        ('Corte/Estamp.', 'Corte/Estamp.'),
        ('T.I - Manuntecao - Rede', 'T.I - Manuntecao - Rede'),
        ('Solda', 'Solda'),
        ('Usinagem', 'Usinagem'),
        ('Gestao de Pessoas', 'Gestao de Pessoas'),
        ('Sesmt', 'Sesmt'),
        ('Expedicao', 'Expedicao'),
        ('Projetos', 'Projetos'),
        ('Financeiro', 'Financeiro'),
        ('Comercial', 'Comercial'),
        ('Pcp', 'Pcp'),
        ('Forjaria/Trat. Termi', 'Forjaria/Trat. Termi'),
        ('Marketing', 'Marketing'),
        ('Gestao Industrial', 'Gestao Industrial'),
        ('Contabilidade', 'Contabilidade'),
    ]
    sector = forms.ChoiceField(choices=SECTOR_CHOICES, required=True) 
    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'name', 'sector']
        
    def clean_sector(self):
        sector = self.cleaned_data.get('sector')
        if not sector:
            raise forms.ValidationError('Por favor, selecione um setor.')
        return sector