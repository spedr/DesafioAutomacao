# language: pt
Funcionalidade: Entrar no Serviço de Internet Banking
  Como um usuário do serviço de internet banking
  Eu quero fazer login na minha conta
  Para que eu possa gerenciar minhas finanças

  Esquema do Cenário: Login com diferentes credenciais
    Dado que estou na página de login
    Quando eu informo o usuário "<usuario>" e a senha "<senha>"
    Então eu devo ser redirecionado base no resultado "<resultado>"

    Exemplos:
      | usuario                     | senha         | resultado    |
      | usuario1@bugbank.com        | 123456        | sucesso      |
      | usuario@invalido.com        | 123456        | falha        |