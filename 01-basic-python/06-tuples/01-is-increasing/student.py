def is_increasing(ns):
    for (x, y) in zip(xs, xs[1:]):
        if x > y:
            return False
    return True 
