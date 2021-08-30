import re # expreçoes regulares

def cpf_valido( numero_do_cpf):
    return len(numero_do_cpf) == 11

def nome_valido( nome):
        return nome.isalpha()

def rg_valido( rg):
        return len(rg) == 9

def celular_valido( celular):
    '''verifica se o celular é valido modelo->11 9 9999-9999'''

    modelo = '([0-9]{2,3})?()?[0-9]{2}( )?[0-9]{5}(-)?[0-9]{4}'
    resposta = re.findall(modelo, celular)
    return resposta
