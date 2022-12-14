def ranked(__iterable, *, key=None, reverse=False):
    if key is None:
        key = lambda x: x

    rank = 0
    prev = None
    for x in sorted(__iterable, key=key, reverse=reverse):
        if prev is None or key(x) != prev:
            rank += 1
        yield rank, x
