from django.db import models


class Categoria(models.Model):  # Cria a classe do model Categoria
    nome = models.CharField(max_length=100)
    # Cria o field nome com o tipo char e tamanho maximo 100
    dt_criacao = models.DateTimeField(auto_now_add=True)
    # Tipo DateTime adicionando a automaticamente a data do SO

    def __str__(self):  # Permite exibir uma string como identificação
        return self.nome  # Exibe o nome como identificação


class Transacao(models.Model):  # Cria a classe de model Transação
    descricao = models.CharField(max_length=200)
    # Cria o field descricao com o tipo char e tamanho maximo 200
    dt_criacao = models.DateTimeField()
    # Tipo DateTime
    valor = models.DecimalField(max_digits=7, decimal_places=2)
    # Tipo decimal, com 7 digitos no total e 2 depois da virgula.
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    # Chava estrangeira p/ a tbl Categoria, relação de 1 pra muitos
    observacao = models.TextField(null=True, blank=True)
    # Tipo text, Pode ser nulo ou vazio...

    def __str__(self):  # Permite exibir uma string como identificação
        return self.descricao  # Exibe a descricao como identificação

    class Meta: # Cria uma classe que usa metadados para ajustar o plural
        verbose_name_plural = "Transacoes"