import cupom;

nome_loja = "Arcos Dourados Com. de Alimentos LTDA"
logradouro = "Av. Projetada Leste"
numero = 500
complemento = "EUC F32/33/34"
bairro = "Br. Sta Genebra"
municipio = "Campinas"
estado = "SP"
cep = "13080-395"
telefone = "(19) 3756-7408"
observacao = "Loja 1317 (PDP)"
cnpj = "42.591.651/0797-34"
inscricao_estadual = "244.898.500.113"

def test_exercicio1():
    assert cupom.imprime_dados_loja() == '''Arcos Dourados Com. de Alimentos LTDA
Av. Projetada Leste, 500 EUC F32/33/34
Br. Sta Genebra - Campinas - SP
CEP:13080-395 Tel (19) 3756-7408
Loja 1317 (PDP)
CNPJ: 42.591.651/0797-34
IE: 244.898.500.113
'''

def test_exercicio2_tudo_vazio():
    global nome_loja
    global logradouro
    global numero
    global complemento
    global bairro
    global municipio
    global estado
    global cep
    global telefone
    global observacao
    global cnpj
    global inscricao_estadual
    
    cupom.nome_loja = ""
    cupom.logradouro = ""
    cupom.numero = 0
    cupom.complemento = ""
    cupom.bairro = ""
    cupom.municipio = ""
    cupom.estado = ""
    cupom.cep = ""
    cupom.telefone = ""
    cupom.observacao = ""
    cupom.cnpj = ""
    cupom.inscricao_estadual = ""

    assert cupom.imprime_dados_loja() == '''
, 0 
 -  - 
CEP: Tel 

CNPJ: 
IE: 
'''

def test_exercicio2_customizado():
    global nome_loja
    global logradouro
    global numero
    global complemento
    global bairro
    global municipio
    global estado
    global cep
    global telefone
    global observacao
    global cnpj
    global inscricao_estadual
    
    # Defina seus próprios valores para as variáveis a seguir
    cupom.nome_loja = "Smelly Cat"
    cupom.logradouro = "Rua Etheria"
    cupom.numero = 205
    cupom.complemento = "Perto da velhinha que mora em uma caverna"
    cupom.bairro = "Br. Templo do Cristal"
    cupom.municipio = "Beach City"
    cupom.estado = "BC"
    cupom.cep = "8051-604"
    cupom.telefone = "(66)4002-8922"
    cupom.observacao = "Por Favor ignorar os exército Intergalácticos em guerra tentando dominar o planeta"
    cupom.cnpj = "53.409.609/0001-85"
    cupom.inscricao_estadual = "512.670.302.653"
    expected = "Smelly Cat\n"
    expected += "Rua Etheria, 205 Perto da velhinha que mora em uma caverna\n"
    expected += "Br. Templo do Cristal - Beach City - BC\n"
    expected += "CEP:8051-604 Tel (66)4002-8922\n"
    expected += "Por Favor ignorar os exército Intergalácticos em guerra tentando dominar o planeta\n"
    expected +="CNPJ: 53.409.609/0001-85\n"
    expected += "IE: 512.670.302.653\n"

    #E atualize o texto esperado abaixo
    assert cupom.imprime_dados_loja() == expected
