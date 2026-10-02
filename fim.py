import datetime
def insert_persian_data(last_data, price, date):
    
    name = last_data[1]
    
    date1_str = last_data[3]
    date2_str = date
    
    date1 = datetime(int(date1_str[0:4]), int(date1_str[5:7]), int(date1_str[8:]))
    date2 = datetime(int(date2_str[0:4]), int(date2_str[5:7]), int(date2_str[8:]))
    
    price1 = last_data[2]
    price2 = price
    
    d = (date2-date1).days
    
    mid_dates = [date1_str]
    a=[]
    for i in range(len(d)):
        a.append(d[i])
    
    return a