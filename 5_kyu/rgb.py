def rgb(r, g, b):
    return (f'{hex(0 if r < 0 else 255 if r > 255 else r)[2:].zfill(2)}'
            f'{hex(0 if g < 0 else 255 if g > 255 else g)[2:].zfill(2)}'
            f'{hex(0 if b < 0 else 255 if b > 255 else b)[2:].zfill(2)}').upper()


print(rgb(1, 275, 3))
