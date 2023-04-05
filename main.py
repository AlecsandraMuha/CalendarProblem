from datetime import datetime, timedelta


def find(calendar1, range1, calendar2, range2, time):
    # merge the calendars and sort based on the start time
    # we use a list called "dates" that contains two lists
    # called "calendar1" and "calendar2",
    # these two list contain information about the availability
    # for meetings between the two persons .
    # the method 'datetime.strptime' is used to convert the type string in
    # the format we want
    # we are sorting the list (in ascending order)
    # the + operator is used to concatenate these two lists into a single list of dates
    dates = sorted(calendar1 + calendar2, key=lambda y: datetime.strptime(y[0], '%H:%M'))

    # we calculate the maximum/minimum of the ranges from the two lists(start range, end range)
    min_range = max(datetime.strptime(range1[0], '%H:%M'), datetime.strptime(range2[0], '%H:%M'))
    max_range = min(datetime.strptime(range1[1], '%H:%M'), datetime.strptime(range2[1], '%H:%M'))

    # Creating a list of free time slots, we are iterating
    # through the list of dates and checking for gaps
    # between consecutive events.
    free_time = []
    x = min_range
    # x=the minimum range that we calculated earlier, which represents
    # the start of the time range in which free time is being searched for.
    for start, end in dates:
        starttime = datetime.strptime(start, '%H:%M')
        endtime = datetime.strptime(end, '%H:%M')
        if starttime > x:
            free_time.append((x, starttime))
        x = max(x, endtime)
    if x < max_range:
        free_time.append((x, max_range))
    # we are calculating the free time and find
    # all the possible cases
    # the start and end times are converted to datetime using the 'strptime' method.

    # available is a list that will contain the final result
    # we use timedelta to convert the meeting time given to minute
    # if the difference between end and start is greater or equal then the meeting time given
    # then we check all the cases possible in our problem
    available = []
    for start, end in free_time:
        if (end - start) >= timedelta(minutes=time):
            if start.time() >= datetime.strptime(range1[0], '%H:%M').time() and \
                    end.time() <= datetime.strptime(range1[1], '%H:%M').time():
                if start.time() >= datetime.strptime(range2[0], '%H:%M').time() and \
                        end.time() <= datetime.strptime(range2[1], '%H:%M').time():
                    available.append([start.strftime('%H:%M'), end.strftime('%H:%M')])
    return available


calendar1 = [['9:00', '10:30'], ['12:00', '13:00'], ['16:00', '18:00']]
range1 = ['9:00', '20:00']
calendar2 = [['10:00', '11:30'], ['12:30', '14:30'], ['14:30', '15:00'], ['16:00', '17:00']]
range2 = ['10:00', '18:30']
meeting_minutes = 30

print(find(calendar1, range1, calendar2, range2, meeting_minutes))
