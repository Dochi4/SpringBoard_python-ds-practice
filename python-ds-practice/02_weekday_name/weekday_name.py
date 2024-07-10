def weekday_name(day_of_week):
    # """Return name of weekday.
    
    #     >>> weekday_name(1)
    #     'Sunday'
        
    #     >>> weekday_name(7)
    #     'Saturday'
        
    # For days not between 1 and 7, return None
    
    #     >>> weekday_name(9)
    #     >>> weekday_name(0)
    # """
    if day_of_week in range(1,5):
        day_list = ['None','Sunday','Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday','None','None']
        return day_list[day_of_week]
    else:
        return "None"
    