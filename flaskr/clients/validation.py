
def validate_basic_clients_data(inputs):
    if "email" not in inputs or "password" not in inputs:
        return False

    if len(inputs['password']) < 3:
        return False

    return True


def validate_register_client_data(inputs):
    is_valid = validate_basic_clients_data(inputs)
    if not is_valid:
        return False

    if "name" not in inputs:
        return False
    return True
