def validate_selection(selection, valid_start, valid_end):
    try:
        selection = int(selection)
    except:
        return False
    if selection in range(valid_start, valid_end):
        return True
    else:
        return False
