
calendar = {}

def print_calendar():
    print(calendar)

def add_event(date, event_name):
    calendar[date] = event_name

def calendar_start():
    add_event("2023-01-01", "New years day party")
    add_event("2023-01-07", "Back to school")
    print_calendar()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    calendar_start()