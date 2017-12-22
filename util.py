import decimal

def float_to_str (f):
    # create a new context for this task
    ctx = decimal.Context()
    # 20 digits should be enough for everyone :D
    ctx.prec = 20
    """
    Convert the given float to a string,
    without resorting to scientific notation
    """
    d1 = ctx.create_decimal(repr(f))
    return format(d1, 'f')
