# Desafio Automação

Este repositório contém suítes de teste que abrangem os requisitos do projeto proposto para o Desafio de automação.

## Instalação

Para instalar as dependências necessárias para executar as suítes de teste, você precisa ter o Python instalado (>=3.10). Após instalar o Python, siga os passos abaixo:

1. Abra o terminal ou prompt de comando.
2. Navegue até o diretório do projeto.
3. Execute o seguinte comando para instalar as dependências:

```bash
pip install -r requirements.txt
```

### Allure

Para a geração do report de tests, que retém a história dos testes, tira screenshots em casos de falha, e captura o stdout em cada step, é recomendada a instalação do Allure. De acordo com o seu sistema, você pode seguir os passos listados na [página de instalação do Allure](https://allurereport.org/docs/gettingstarted-installation/).

Caso a instalação do Allure não seja possível, é necessário alterar o valor de `REPORT_ENGINE` no arquivo `config.py` na raíz do projeto para `junit`.

## Configurações do Arquivo `config.py`

O arquivo `config.py` contém várias configurações que controlam o comportamento das suítes de teste. Abaixo está a descrição de cada configuração disponível:

### Motor de Relatório
- `REPORT_ENGINE`: Define o tipo de motor de relatório a ser usado para gerar relatórios de teste. As opções disponíveis são:
  - `"allure"`: Usa o Allure para geração de relatórios.
  - `"junit"`: Usa o [junit2html](https://github.com/inorton/junit2html) para geração de um report mais simples, caso a instalação do Allure não seja possível.
  
### Verbosidade
- `VERBOSE`: Quando definido como `True`, aumenta a verbosidade do log dos testes.

### Abrir Relatório no navegador automaticamente
- `AUTO_OPEN_REPORT`: Quando definido como `True`, abre automaticamente o relatório gerado no navegador após a conclusão dos testes.

### Timeout Padrão
- `DEFAULT_TIMEOUT`: Especifica o tempo máximo de espera em segundos para as operações durante os testes.

### Opções do Navegador
- `BROWSER_HEADLESS`: Quando definido como `True`, executa os testes no modo headless (sem interface gráfica).
- `BROWSER_TYPE`: Define o tipo de navegador a ser usado para os testes. As opções disponíveis são `"chrome"` e `"firefox"`.
- `BROWSER_LOCALE`: Define a localidade do navegador. O padrão é `"pt-BR"` para Português Brasileiro, mas pode ser alterado para `"en-US"` para Inglês Americano, etc.

### junit2html
- `JUNIT_RESULTS_PATH`: Define o caminho do diretório onde os resultados dos testes no formato JUnit serão salvos. O caminho padrão é `./junit-results`.
- `HTML_REPORTS_PATH`: Define o caminho do diretório onde os relatórios HTML, gerados a partir dos resultados do JUnit, serão salvos. O caminho padrão é `./junit-html-reports`.