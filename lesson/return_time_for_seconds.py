"""(format_duration(1), "1 second")
(format_duration(62), "1 minute and 2 seconds")
(format_duration(120), "2 minutes")
(format_duration(3600), "1 hour")
(format_duration(3662), "1 hour, 1 minutes")"""


def format_duration(seconds):
    value = ''
    time = [31536000, 86400, 3600, 60, 1]
    unit = [' years', ' days', ' hours', ' minutes', ' seconds']
    i = 0
    count = 0
    if seconds == 0:
        return 'now'
    while seconds > 0:
        if seconds // time[i] > 1:
            if seconds % time[i] > 0:
                value += str(seconds//time[i]) + unit[i] + ', '
            elif seconds % time[i] == 0 and count > 0:
                value = value.strip()[:-1] + ' and ' + str(seconds//time[i]) + unit[i]
            else:
                value += str(seconds//time[i]) + unit[i]
            count += 1
        if seconds//time[i] == 1:
            if seconds % time[i] > 0:
                value += str(seconds//time[i]) + unit[i][:-1] + ', '
            elif seconds % time[i] == 0 and count > 0:
                value = value.strip()[:-1] + ' and ' + str(seconds//time[i]) + unit[i][:-1]
            else:
                value += str(seconds//time[i]) + unit[i][:-1]
            count += 1
        seconds = seconds % time[i]
        i += 1
    return value



print(format_duration(3600000004))


times = [("year", 365 * 24 * 60 * 60),
         ("day", 24 * 60 * 60),
         ("hour", 60 * 60),
         ("minute", 60),
         ("second", 1)]

def format_duration(seconds):

    if not seconds:
        return "now"

    chunks = []
    for name, secs in times:
        qty = seconds // secs
        if qty:
            if qty > 1:
                name += "s"
            chunks.append(str(qty) + " " + name)

        seconds = seconds % secs

    return ', '.join(chunks[:-1]) + ' and ' + chunks[-1] if len(chunks) > 1 else chunks[0]