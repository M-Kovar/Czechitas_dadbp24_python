# Funkce access_account(user) ilustruje overovani, jestli uzivatel 
# muze vstoupit do uctu na webove strance podle informaci ve slovniku 'user'

# Bad example
# Ve vnorenych podminkach se spatne orientuje a hure se provadi upravy
def access_account(user):
    if user['is_active']:
        if user['has_permission']:
            if user['is_verified']:
                return "Access granted"
            else:
                return "Access denied: User not verified"
        else:
            return "Access denied: No permission"
    else:
        return "Access denied: User is inactive"


# Good example
# Prehlednejsi je postupne vyloucit vsechny "zakazane stavy" jednoduchymi ify
def access_account(user):
    if not user['is_active']:
        return "Access denied: User is inactive"
    
    if not user['has_permission']:
        return "Access denied: No permission"
    
    if not user['is_verified']:
        return "Access denied: User not verified"
    
    return "Access granted"
