#

def rgb(r, g, b):
    if r < 0: r = 0
    elif r > 255: r = 255

    if g < 0: g = 0
    elif g > 255: g = 255

    if b < 0: b = 0
    elif b > 255: b = 255

    new_r = hex(r)
    if len(new_r) > 2: new_r = new_r[2:]
    if len(new_r) < 2: new_r = "0" + new_r

    new_g = hex(g)
    if len(new_g) > 2: new_g = new_g[2:]
    if len(new_g) < 2: new_g = "0" + new_g

    new_b = hex(b)
    if len(new_b) > 2: new_b = new_b[2:]
    if len(new_b) < 2: new_b = "0" + new_b

    return f'{new_r}{new_g}{new_b}'.upper()

print(rgb(254,253,252))
print(rgb(-20,275,125))