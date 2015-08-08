def email_validator(email):
    from django.core.validators import validate_email
    try:
        validate_email(email)
        return True
    except:
        return False


def order_validator(order_info):
    import re

    errors = []
    checked_order_info = {}

    # Check order_contact_name
    if len(order_info['order_contact_name']) == 0:
        errors.append("a valid contact name is required")
    else:
        checked_order_info['order_contact_name'] = order_info['order_contact_name']

    # Check order_contact_phone and order_contact_email
    if not order_info['order_contact_phone'] and not order_info['order_contact_email']:  # if both items are omitted...
        errors.append("A valid email address or phone number is required")
    else:
        # Check order_contact_phone if it was supplied
        if order_info['order_contact_phone']:
            phone_number = re.sub("[^0-9]", "", order_info['order_contact_phone'])  # strip out any non-numeric chars...
            # If what's left is exactly 10 digits, consider is cleaned and pass it along...
            if len(phone_number) == 10:
                checked_order_info['order_contact_phone'] = phone_number
            # If it's 7 digits, assume it's a '336' area code and add it in
            elif len(phone_number) == 7:
                phone_number = int(''.join(['336', phone_number]))
                checked_order_info['order_contact_phone'] = phone_number
            else:
                errors.append("The provided phone number is invalid")

        # check order_contact_email if it was supplied
        if order_info['order_contact_email']:
            if email_validator(order_info['order_contact_email']):
                checked_order_info['order_contact_email'] = order_info['order_contact_email']
            else:
                errors.append("The provided email address is invalid")
    return {'order_info': checked_order_info, 'errors': errors}
