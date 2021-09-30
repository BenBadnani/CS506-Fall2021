def custom_parser(text):
    in_quotes = False
    df = []
    current_row = 0
    current_column = 0
    current_elem = ""
    current_row = []
    for char in text:
        if char == '"' and in_quotes == False:
            in_quotes = True
        elif char == '"' and in_quotes == True:
            in_quotes = False
        else:   
            # in quote mode
            if in_quotes == True:
                # no matter what item it is, append it to the current element
                current_elem += char
            # if we're not in quote mode 
            else:
                # if the next item is a commma, then append current_elem to that index, increment index and reset current_elem
                if char == ",":
                    current_row.append(current_elem)
                    current_elem = ""
                # if the next item is a newline, not in quote mode, then append the entire row to the data frame, and reset the current_elem and current_row
                elif char == "\n":
                    current_row.append(current_elem)
                    df.append(current_row)
                    current_row = []
                    current_elem = ""
                else:
                    current_elem += char
    return df


def read_csv(csv_file_path):
    """
        Given a path to a csv file, return a matrix (list of lists)
        in row major.
    """

    ret_df = []
    
    f = open(csv_file_path)
    text = f.read()
    
    return custom_parser(text)
