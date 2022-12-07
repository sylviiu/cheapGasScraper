def get(string, maxCharLength = None):
    toAdd = None
    while toAdd is None:
        pending = input(string + " ")
        if isinstance(maxCharLength, int) and maxCharLength is len(pending):
            toAdd = pending
            print("Successfully set as \"" + pending + "\"")
        elif not isinstance(maxCharLength, int):
            toAdd = pending
            print("Successfully set as \"" + pending + "\"")
        else:
            print("Could not set as \"" + pending + "\" -- must be a length of " + str(maxCharLength))
    return toAdd