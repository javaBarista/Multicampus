def count_char(instr):
    nc, lc, uc, hc, ec = [0] * 5

    for i in instr:
        c = ord(i)

        if c >= ord("A") and c <= ord("Z"): uc += 1
        elif c >= ord("a") and c <= ord("z"): lc += 1
        elif c >= ord("0") and c <= ord("9"): nc += 1
        elif c >= ord("가") and c <= ord("힣"): hc += 1
        else: ec += 1

    return {'upper' : uc, 'lower' : lc, 'number' : nc, 'kor' : hc, 'etc' : ec} 
