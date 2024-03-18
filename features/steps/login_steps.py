from behave import given, when, then
from page_objects.login_page import LoginPage
from page_objects.home_page import HomePage

@given('que estou na página de login')
def step_impl(context):
    context.driver.get("https://bugbank.netlify.app")
    context.login_page = LoginPage(context.driver)

@when('eu informo o usuário "{usuario}" e a senha "{senha}"')
def step_impl(context, usuario, senha):
    context.login_page.login(usuario, senha)

@then('eu devo ser redirecionado base no resultado "{resultado}"')
def step_impl(context, resultado):
    if resultado == "sucesso":
        home_page = HomePage(context.driver)
        assert home_page.is_greeting_displayed(), "Texto de saudação não exibido na página inicial."
        numero_conta = home_page.get_account_number()
        assert numero_conta, "Número da conta não exibido na página inicial."
        saldo = home_page.get_balance()
        assert saldo, "Saldo não exibido na página inicial."    
    elif resultado == "falha":
        assert context.login_page.is_login_failure_modal_displayed(), "Modal de falha no login não é exibido."
        mensagem_erro = context.login_page.get_login_failure_message()
        mensagem_esperada = "Usuário ou senha inválido.\nTente novamente ou verifique suas informações!".strip()
        assert mensagem_erro == mensagem_esperada, f"Mensagem de erro esperada '{mensagem_esperada}', mas obteve '{mensagem_erro}'."
        context.login_page.close_login_failure_modal()

@then('eu faço logout')
def step_impl(context):
    home_page = HomePage(context.driver)
    home_page.click_exit()