# pySerasa para Json

O pySerasa para Json é uma lib python baseada no pySerasa do [Luiz Felipe do Divino](https://github.com/lfdivino), porém alterado para atender necessidades onde precisamos do retorno estruturadop em formato de json.

Atualmente esta lib faz a consulta por CPF e retorna os seguintes dados estruturados:

```
json = {
        'nomeCompleto':'',
        'dataNascimento':'',
        'nomeMae':'',
        'pendenciasInternas':
          {
            'ocorrencias': '',
            'valorTotal': '',
            'descricao' : '',
          },
        'pendenciasFinanceiras':
          {
            'ocorrencias': '',
            'valorTotal': '',
            'descricao' : '',
          },
        'chequesSemFundo':
          {
            'ocorrencias': '',
            'valorTotal': '',
            'descricao' : '',
          },
        'protestos':
          {
            'ocorrencias': '',
            'valorTotal': '',
            'descricao' : '',
          },
        'chequesSemFundo':'',
        'score':'',

    }
```

Para usar a lib é bem simples, basta importar a lib e então chamar o parser conforme o example.py orienta. 
*Importante*: já incluímos uma massa de dados no example.py para que possa validar suas consultas.


# Dúvidas e melhorias
Caso tenha sugestões ou queira contribuir, pode entrar em contato ou fazer pull requests :) Serão sempre bem vindas.


Contribuidores.
---
- [Luiz Felipe do Divino](https://github.com/lfdivino)
- [oAlexandre](https://github.com/oalexandre)
- [Aupi Soluções em TI](https://www.aupi.com.br)

# Fork de KMEE Módulo pySerasa - Serasa Crednet
- [Forked from lfdivini](https://github.com/lfdivino)

