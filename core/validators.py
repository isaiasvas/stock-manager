import re
from django.core.exceptions import ValidationError

def validar_cnpj(value):
    if not re.match(r'^\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}$', value):
        raise ValidationError("CNPJ inválido. Formato esperado: 00.000.000/0000-00")

def validar_cpf(value):
    if not re.match(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$', value):
        raise ValidationError("CPF inválido. Formato esperado: 000.000.000-00")

def validar_codigo_bacen(value):
    if not re.match(r'^\d+$', value):
        raise ValidationError("Código BACEN deve conter apenas números.")
