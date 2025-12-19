from datetime import datetime

def get_days_from_today(date_str):
    try:
        given_date = datetime.strptime(date_str, "%Y-%m-%d").date()
        today = datetime.today().date()
        return (today - given_date).days
    except ValueError:
        return None
