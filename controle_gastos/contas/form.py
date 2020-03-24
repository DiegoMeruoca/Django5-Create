from django.forms import ModelForm  # Importa o ModelForm, classe que traz
# recursos que facilitam a criação de forms... como validações, por exemplo
from .models import Transacao  # Importa o model Transacao


class TransacaoForm(ModelForm):  # Cria a classe que herda os atributos e
    # metodos da classe ModelForm
    class Meta:  # Cria uma classe que usa metadados
        model = Transacao  # Define omodel do form
        fields = ['descricao','dt_criacao','valor','categoria','observacao']
        # Define os fields (Campos) do form
