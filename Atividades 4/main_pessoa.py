from Pessoa import Pessoa
from PessoaFisica import PessoaFisica
from PessoaJuridica import PessoaJuridica

pessoa = Pessoa(
    nome="Carlos",
    numeroConta="12345",
    dataAberturaConta="2024-01-01",
    status=True
)

print('Instancia da classe Pessoa:')
print(pessoa.imprimir())


pessoa_fisica = PessoaFisica(
    nome="Ana",
    numeroConta="67890",
    dataAberturaConta="2023-01-01",
    status=False,
    dataNascimento="1990-05-15",
    cpf="111.222.333-44",
    rg="12345678-9"
)

print('\nInstancia da classe PessoaFisica:')
print(pessoa_fisica.imprimir())

pessoa_juridica = PessoaJuridica(
    nome="Empresa XYZ",
    numeroConta="54321",
    dataAberturaConta="2022-12-01",
    status=True,
    dataAberturaEmpresa="2022-12-01",
    cnpj="00.000.000/0001-00"
)

print('\nInstancia da classe PessoaJuridica:')
print(pessoa_juridica.imprimir())

try:
    pessoa_fisica.cpf = "123456789"
except ValueError as e:
    print(f"\nErro ao definir CPF: {e}")

try:
    pessoa_juridica.cnpj = "00.000.000/0001-01"
except ValueError as e:
    print(f"\nErro ao definir CNPJ: {e}")

pessoa_fisica.cpf = "000.111.222-33"
pessoa_juridica.cnpj = "11.222.333/0001-11"

print('\nApós alterações:')
print(pessoa.imprimir())
print(pessoa_fisica.imprimir())
print(pessoa_juridica.imprimir())