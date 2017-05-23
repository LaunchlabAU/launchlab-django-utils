def currency_display(value, currency='AUD', show_complete=False, include_sign=True):
    """
    Create a human readable string to display a currency from some number of smallest units (e.g. cents). 

    :param value: value of currency in smallest units (cents) 
    :param currency: e.g. 'AUD'
    :param show_complete: if True, show '$5.00' rather than '$5'
    :param include_sign: Include the e.g. dollar sign
    :return: 
    """
    if currency != 'AUD':
        raise NotImplementedError('Only AUD currently supported')

    unit_modulo = 100
    large_units = int(value / unit_modulo)
    small_units = value % unit_modulo
    sign = '$' if include_sign else ''
    if show_complete or small_units:
        return '{sign}{large}.{small:02}'.format(sign=sign, large=large_units, small=small_units)
    else:
        return '{sign}{large}'.format(sign=sign, large=large_units)
