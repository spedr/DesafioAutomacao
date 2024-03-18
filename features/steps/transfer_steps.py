import re
from behave import given, when, then
from page_objects.login_page import LoginPage
from page_objects.home_page import HomePage
from page_objects.transfer_page import TransferPage


@given('que eu tenho o saldo inicial da conta destino "{email_destino}" com a senha "{pwd_destino}"')
def step_impl(context, email_destino, pwd_destino):
    # This step stores the initial balance of the destination account before the transfer
    context.initial_balance_destino = check_and_store_balance(context, email_destino, pwd_destino, logout=True)
    print(f"Saldo inicial verificado para a conta destino {email_destino}: R$ {context.initial_balance_destino}")

@given('estou logado na conta "{email_origem}" com a senha "{pwd_origem}"')
def step_impl(context, email_origem, pwd_origem):
    context.initial_balance_origem = check_and_store_balance(context, email_origem, pwd_origem, logout=False)

@when('acesso a página de transferência')
def step_impl(context):
    home_page = HomePage(context.driver)
    home_page.click_element(home_page.TRANSFER_BUTTON)
    context.transfer_page = TransferPage(context.driver)
    assert context.transfer_page.is_element_visible(context.transfer_page.TRANSFER_BUTTON), "Não está na página de transferência."

@when('eu preencho os dados da transferência para a conta "{conta_destino}" com o valor "{valor_transferencia}"')
def step_impl(context, conta_destino, valor_transferencia):
    context.transfer_page.fill_account_number(conta_destino.split("-")[0])
    context.transfer_page.fill_account_digit(conta_destino.split("-")[1])
    context.transfer_page.fill_transfer_value(valor_transferencia)
    context.transfer_page.fill_description("Teste")

@when('clico no botão de realizar transferência')
def step_impl(context):
    context.transfer_page.submit_transfer()

@then('a transferência é realizada com sucesso')
def step_impl(context):
    transfer_page = TransferPage(context.driver)
    assert transfer_page.is_transfer_successful(), "A transferência não foi realizada com sucesso ou a mensagem de sucesso não foi exibida."
    transfer_page.close_modal()


@then('é exibida uma mensagem de erro informando saldo insuficiente')
def step_impl(context):
    transfer_page = TransferPage(context.driver)
    assert transfer_page.is_insufficient_funds_error_displayed(), "A mensagem de erro de saldo insuficiente não foi exibida."
    transfer_page.close_modal()

def check_and_store_balance(context, email, password, logout=True):
    """Utility function that quickly logs into an account, checks the balance, and optionally logs out."""
    login_page = LoginPage(context.driver)
    home_page = HomePage(context.driver)
    
    # Perform login
    login_page.login(email, password)
    
    # Retrieve and print the balance
    balance_text = home_page.get_balance()
    balance = re.search(r'R\$ ([\d.,]+)', balance_text).group(1)
    balance_float = float(balance.replace('.', '').replace(',', '.'))
    
    # Print the obtained balance for the account
    print(f"Saldo verificado para a conta {email}: R$ {balance}")

    # Logout if specified
    if logout:
        home_page.click_exit()
    
    return balance_float

@given('tenho saldo suficiente para uma transferência de "{valor_transferencia}"')
def step_impl(context, valor_transferencia):
    # Assumes context has balance stored
    assert context.initial_balance_origem >= float(valor_transferencia.replace('.', '').replace(',', '.')), "Saldo insuficiente para a transferência."

@given('não tenho saldo suficiente para uma transferência de "{valor_transferencia}"')
def step_impl(context, valor_transferencia):
    # Assumes context has balance stored
    assert context.initial_balance_origem < float(valor_transferencia.replace('.', '').replace(',', '.')), "Saldo insuficiente para a transferência."

@then('o meu saldo permanece inalterado')
def step_impl(context):
    home_page = HomePage(context.driver)
    home_page.click_back()

    balance_text = home_page.get_balance()
    balance = re.search(r'R\$ ([\d.,]+)', balance_text).group(1)
    balance_float = float(balance.replace('.', '').replace(',', '.'))
    assert context.initial_balance_origem == balance_float, "Valor é diferente do original em transação não concluída."