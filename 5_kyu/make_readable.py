def make_readable(seconds):
    hr = seconds // 3600
    min = (seconds - (hr * 3600)) // 60
    sec = seconds - (hr * 3600) - (min * 60)

    return f'{hr:02}:{min:02}:{sec:02}'


print(make_readable(59))  # "00:00:59"
print(make_readable(60))  # "00:01:00"
print(make_readable(3599))  # "00:59:59"
