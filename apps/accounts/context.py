import threading
thread_local = threading.local()

def get_current_company():
    return getattr(thread_local, 'company_id', None)

def set_current_company(company_id):
    thread_local.company_id = company_id

def get_current_user_is_superuser():
    """Retorna True se o usuário atual for um Superusuário."""
    # O valor padrão é False para segurança.
    return getattr(thread_local, 'is_superuser', False)

def set_current_user_is_superuser(is_superuser):
    """Define o status de Superusuário na thread atual."""
    thread_local.is_superuser = is_superuser