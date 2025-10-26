# Import dependencies
import re

def validate_cep(cep):
    # Strip all non-digits
    cep_clean = re.sub(r'\D', '', cep)

    # Must be exactly 8 digits
    if len(cep_clean) != 8:
        return False, "CEP must contain exactly 8 digits"

    # Return success and cleaned cep
    return True, cep_clean
