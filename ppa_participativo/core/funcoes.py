# -*- coding: utf-8 -*-


def mascara_cpf(dados):
    """
    aplica mascara de CPF, completando com zeros à esquerda quando necessário
    """
    cpf = str(dados).rjust(11, '0')
    return cpf[-len(cpf):-8]+'.'+cpf[-8:-5]+'.'+cpf[-5:-2]+'-'+cpf[-2:]


def mascara_cnpj(dados):
    """
    aplica mascara de CNPJ, completando com zeros à esquerda quando necessário
    """
    cnpj = str(dados).rjust(14, '0')
    return cnpj[-len(cnpj):-12]+'.'+cnpj[-12:-9]+'.'+cnpj[-9:-6]+'/'+cnpj[-6:-2]+'-'+cnpj[-2:]


def valida_cpf(cpf):
    """
    Essa Função tem o código que efetivamente valida o CPF da pessoa
    """
    cpfNum = []
    if cpf in [''.rjust(11, '0'), ''.rjust(11, '1'), ''.rjust(11, '2'), ''.rjust(11, '3'), ''.rjust(11, '4'),
               ''.rjust(11, '5'), ''.rjust(11, '6'), ''.rjust(11, '7'), ''.rjust(11, '8'), ''.rjust(11, '9')]:
        return False
    else:
        for i in cpf:
            try:
                cpfNum.append(int(i))
            except:
                pass
        soma = 0
        produto = 10
        for x in cpfNum[:9]:
            soma = soma + (produto * x)
            produto = produto - 1
        valor = (soma / 11) * 11
        resultado = soma - valor
        digito1 = None
        if resultado == 0 or resultado == 1:
            digito1 = 0
        else:
            digito1 = 11 - resultado
        soma2 = 0
        produto2 = 11
        for q in cpfNum[:9]:
            soma2 = soma2 + (produto2 * q)
            produto2 = produto2 - 1
        soma2 = soma2 + (digito1 * 2)
        valor2 = (soma2 / 11) * 11
        resultado2 = soma2 - valor2
        digito2 = None
        if resultado2 == 0 or resultado2 == 1:
            digito2 = 0
        else:
            digito2 = 11 - resultado2

        if digito1 == cpfNum[9] and digito2 == cpfNum[10]:
            return True

        return False


def valida_cnpj(cnpj_orig):
    """
    Valida o número de CNPJ
    """
    if cnpj_orig in [''.rjust(14, '0'), ''.rjust(14, '1'), ''.rjust(14, '2'), ''.rjust(14, '3'), ''.rjust(14, '4'),
                     ''.rjust(14, '5'), ''.rjust(14, '6'), ''.rjust(14, '7'), ''.rjust(14, '8'), ''.rjust(14, '9')]:
        return False
    else:
        cnpj_orig = map(int, cnpj_orig)
        cnpj = cnpj_orig[:12]
        prod = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        # pegamos apenas os 9 primeiros dígitos do CNPJ e geramos os
        # dois dígitos que faltam
        while len(cnpj) < 14:

            r = sum([x*y for (x, y) in zip(cnpj, prod)]) % 11

            if r > 1:
                f = 11 - r
            else:
                f = 0
            cnpj.append(f)
            prod.insert(0, 6)

        # se o número com os digítos faltantes coincidir com o número
        # original, então ele é válido
        print cnpj, cnpj_orig
        return bool(cnpj == cnpj_orig)
