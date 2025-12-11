from datetime import datetime

def get_days_from_today(date_str):
    given_date = datetime.strptime(date_str, "%Y-%m-%d").date()
    
    today = datetime.today().date()
    
    delta = today - given_date
    
    return delta.days
print(get_days_from_today("2020-10-09"))
