def bisection_method(f, a, b, eps):
    if f(a) * f(b) > 0:
        raise Exception("your limits suck")

    while (abs(b - a) > 2 * eps):
        mid = (a + b) / 2
        if (f(a) * f(mid) > 0):
            a = mid
        else:
            b = mid

    return (a + b) / 2
