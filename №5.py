def convert_to_12_hour_format(h,m):
    if h > 12:
        return f'{h-12}:{m} PM'
    else:
        return f'{h}:{m} AM'


print(convert_to_12_hour_format(23,42))