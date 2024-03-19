# Bugs identificados

Esse documento lista alguns dos bugs identificados durante o processo de teste. Como o exerício foi abordado de uma perspectiva de uma implementação de uma suíte de regressão end-to-end e os critérios de aceite não são documentados, a detecção desses bugs não foi contemplada de maneira automatizada. De toda forma, vale listar alguns.

### Erro de arredondamento ao realizar uma transação com valor não-inteiro

Ao realizar uma transfêrencia entre contas com qualquer valor não-inteiro e que não possui uma equivalência exata em binário (por exemplo ~x.66, x.33, x.03, x.06...) de acordo com o padrão [IEEE 754 para aritmética de ponto flutuante](https://en.wikipedia.org/wiki/IEEE_754). O resultado são números como os abaixo sendo registrados no saldo.

![Erro de arrendondamento](https://i.imgur.com/X9rsbgP.png)


### Transferências com valores de mais de duas casas depois da vírgula

É possível transacionar com valores de mais de duas casas depois da vírgula, o que deveria ser impossível. Originalmente a função `format_value_according_to_locale` tinha sido escrita para manter a entrada consistente e não permitir valores com mais de duas casas, mas o comportamento foi removido para refletir o comportamento do front. Ademais, os valores gerados por erro de arredondamento de aritmética de ponto flutuante (bug anterior) podem ser utilizados para transacionar dessa forma também. Abaixo segue uma imagem de exemplo.

![Transferências com números com mais de duas casas depois da vírgula](https://i.imgur.com/pqsHKot.png)

### Transferências para mesma conta são redirecionadas para a tela de extrato

Ao fazer uma transferência de mesma origem e destino, o sistema corretamente alerta que não é possível transferir para a mesma conta. O saldo também não é movimentado. No entanto, o usuário é redirecionado para a tela de extrato, o que não ocorre em outros cenários. Ademais, ao apertar no botão "Voltar", o usuário não é redirecionado de volta para a home, e sim de volta para a tela de transferências, um comportamento que não é possível dentro de circunstâncias normais.

### Campo "Valor da transferência" não aceita valores separados por vírgula

O campo valor da transferência requer uma entrada com separador decimal `.` (padrão internacional). Foram feitos testes trocando o locale do navegador (a configuração `BROWSER_LOCALE` tinha sido implementada para esta finalidade), embora o comportamento observado é mantido em qualquer locale.