def convert_to_12_hour_format(hours,minutes)
    if hours > 12:
        return f'{hours-12}:{minutes} PM'
    else:
        return f'{hours}:{minutes} AM'


print(convert_to_12_hour_format(23,42))
