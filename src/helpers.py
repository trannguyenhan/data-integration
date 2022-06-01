def fill_none_value_header(header):
    cnt = 1

    new_header = []
    for item in header:
        new_item = item 
        if item == None or item == "": 
            name_column = "col" + str(cnt)
            cnt += 1
            new_item = name_column
        new_header.append(new_item)
    
    return new_header