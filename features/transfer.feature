# language: pt

Funcionalidade: Realizar Transferência Entre Contas
  Como um usuário do serviço de internet banking
  Eu quero realizar transferências entre contas
  Para que eu possa enviar dinheiro para outras contas

  Esquema do Cenário: Transferência entre contas com verificação prévia e posterior do saldo
    Dado que eu tenho o saldo inicial da conta destino "<email_destino>" com a senha "<pwd_destino>"
    E estou logado na conta "<email_origem>" com a senha "<pwd_origem>"
    E tenho saldo suficiente para uma transferência de "<valor_transferencia>"
    Quando acesso a página de transferência
    Quando eu preencho os dados da transferência para a conta "<conta_destino>" com o valor "<valor_transferencia>"
    E clico no botão de realizar transferência
    Então a transferência é realizada com sucesso
    E eu faço logout

    Exemplos:
      | email_origem           | pwd_origem | email_destino          | conta_destino | pwd_destino | valor_transferencia |
      | usuario1@bugbank.com   | 123456     | usuario2@bugbank.com   | 234-5         | password1   | 500                 |
      | usuario1@bugbank.com   | 123456     | usuario2@bugbank.com   | 234-5         | password1   | 200,44              |
  
  Esquema do Cenário: Tentativa de transferência sem saldo suficiente
    Dado que eu tenho o saldo inicial da conta destino "<email_destino>" com a senha "<pwd_destino>"
    E estou logado na conta "<email_origem>" com a senha "<pwd_origem>"
    E não tenho saldo suficiente para uma transferência de "<valor_transferencia>"
    Quando acesso a página de transferência
    Quando eu preencho os dados da transferência para a conta "<conta_destino>" com o valor "<valor_transferencia>"
    E clico no botão de realizar transferência
    Então é exibida uma mensagem de erro informando saldo insuficiente
    E o meu saldo permanece inalterado
    E eu faço logout

  Exemplos:
  | email_origem           | pwd_origem | email_destino          | conta_destino | pwd_destino | valor_transferencia |
  | usuario1@bugbank.com   | 123456     | usuario2@bugbank.com   | 234-5         | password1   | 1500                |
  | usuario1@bugbank.com   | 123456     | usuario2@bugbank.com   | 234-5         | password1   | 12000,88            |
