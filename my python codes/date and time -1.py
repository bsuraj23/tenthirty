from datetime import datetime,timedelta

#we should take in string format
start_date_str="2025-08-01"
end_date_str="2025-08-06"

#convert the string into datetime format
start_date=datetime.strptime(start_date_str,"%Y-%m-%d")
end_date=datetime.strptime(end_date_str, "%Y-%m-%d")

#loop from start date to end date
current_date= start_date
while current_date<=end_date:
    print(current_date.strftime("%Y-%m-%d"))
    current_date += timedelta(days=1)

# from datetime import datetime, timedelta

# # Define the start and end date as strings (in YYYY-MM-DD format)
# start_date_str = "2025-08-01"
# end_date_str = "2025-08-05"

# # Convert string to datetime objects
# start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
# end_date = datetime.strptime(end_date_str, "%Y-%m-%d")

# # Loop from start_date to end_date
# current_date = start_date
# while current_date <= end_date:
#     print(current_date.strftime("%Y-%m-%d"))
#     current_date += timedelta(days=1)
