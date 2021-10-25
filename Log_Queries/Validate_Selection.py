def validate_selection(selection, valid_end):
    try:
        selection = int(selection)
    except:
        return False
    if selection in range(1, valid_end):
        return True
    else:
        return False
