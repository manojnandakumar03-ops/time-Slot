
from django.shortcuts import render
from .models import TimeSlot

def timetable_view(request):

    days = [
        'Monday',
        'Tuesday',
        'Wednesday',
        'Thursday',
        'Friday',
        'Saturday'
    ]

    time_slots = [
        ('08:00', '10:00'),
        ('10:00', '12:00'),
        ('12:00', '13:00'),
        ('13:00', '15:00'),
        ('15:00', '17:00')
    ]

    records = TimeSlot.objects.all()

    timetable_rows = []

    for start, end in time_slots:

        row = {
            'time': start + ' - ' + end,
            'subjects': []
        }

        for day in days:

            slot = records.filter(
                day__iexact=day,
                start_time__hour=int(start[:2]),
                end_time__hour=int(end[:2])
            ).first()

            row['subjects'].append(
                slot.subject_name if slot else ''
            )

        timetable_rows.append(row)

    return render(request, 'timetable/timetable.html', {
        'days': days,
        'timetable_rows': timetable_rows,
        'has_records': records.exists()
    })
