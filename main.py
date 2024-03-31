def add_time(start, duration, weekday=None):

    #start hours and minutes
    start_hours = int(start.split(':')[0])
    start_min = int(start.split(':')[1].split()[0])

    #duration hours and minutes
    dur_hours = int(duration.split(':')[0])
    dur_min = int(duration.split(':')[1])

    #AM or PM
    if 'A' in start:
        if start_hours == 12:
            start_hours = 0
        else:
            pass
    if 'P' in start:
        if start_hours == 12:
            start_hours = 12
        else:
            start_hours += 12

    #if 60-start_min < dur_min
    if (60 - start_min) < dur_min:
        dur_hours += 1

    #new time to 24 hr clock
    new_time_hours = (start_hours + dur_hours) % 24 
    new_time_min = (start_min + dur_min) % 60

    if new_time_min < 10:
        new_time_min = '0' + str(new_time_min)

    #if new_time_hour = 0, make it 12
    if new_time_hours == 0:
        new_time_hours = 12
        new_time = str(new_time_hours) + ':' + str(new_time_min) + ' AM'
    elif new_time_hours == 12:
        new_time = str(new_time_hours) + ':' + str(new_time_min) + ' PM'
    elif new_time_hours > 12:
        new_time_hours -= 12
        new_time = str(new_time_hours) + ':' + str(new_time_min) + ' PM'
    else:
        new_time = str(new_time_hours) + ':' + str(new_time_min) + ' AM'

    #calculate number of day
    if ((24 - start_hours) < (dur_hours % 24)) or ((start_hours == 23) and (60 - start_min) < dur_min):
        day = dur_hours // 24 + 1
    else:
        day = dur_hours // 24

    if weekday is not None:
        weekdays = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        day_number = weekdays.index(weekday.lower())

        if day < 1:
            new_time += ', ' + weekdays[day_number].title()
            return new_time
        elif day == 1:
            day_number += 1
            new_time += ', ' + weekdays[day_number % 7].title() + ' (next day)'
            return new_time
        elif day > 1:
            day_number += day
            new_time += ', ' + weekdays[day_number % 7].title() + ' (' + str(day) + ' days later)'
            return new_time

    #if weekday is None
    else:
        if day < 1:
            return new_time
        elif day == 1:
            new_time += ' (next day)'
            return new_time
        elif day > 1:
            new_time += ' (' + str(day) + ' days later)'
            return new_time

