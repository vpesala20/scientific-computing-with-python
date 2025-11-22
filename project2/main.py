def add_time(start, duration, starting_day=None):
    # Days of the week for reference
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    # Split start time
    start_time, period = start.split()
    start_hour, start_minute = map(int, start_time.split(':'))

    # Convert start_hour to 24-hour format
    if period.upper() == 'PM' and start_hour != 12:
        start_hour += 12
    elif period.upper() == 'AM' and start_hour == 12:
        start_hour = 0

    # Split duration
    duration_hour, duration_minute = map(int, duration.split(':'))

    # Add hours and minutes
    total_minutes = start_minute + duration_minute
    extra_hour = total_minutes // 60
    final_minute = total_minutes % 60

    total_hours = start_hour + duration_hour + extra_hour
    days_later = total_hours // 24
    final_hour_24 = total_hours % 24

    # Convert back to 12-hour format
    if final_hour_24 == 0:
        final_hour = 12
        final_period = 'AM'
    elif final_hour_24 < 12:
        final_hour = final_hour_24
        final_period = 'AM'
    elif final_hour_24 == 12:
        final_hour = 12
        final_period = 'PM'
    else:
        final_hour = final_hour_24 - 12
        final_period = 'PM'

    # Format minutes with leading zero
    final_minute_str = str(final_minute).rjust(2, '0')

    # Calculate the day of the week if starting_day is given
    day_string = ''
    if starting_day:
        starting_day_index = days_of_week.index(starting_day.capitalize())
        new_day_index = (starting_day_index + days_later) % 7
        day_string = f', {days_of_week[new_day_index]}'

    # Add days later info
    if days_later == 1:
        days_later_str = ' (next day)'
    elif days_later > 1:
        days_later_str = f' ({days_later} days later)'
    else:
        days_later_str = ''

    # Build final string
    new_time = f"{final_hour}:{final_minute_str} {final_period}{day_string}{days_later_str}"
    return new_time