#Abbreviate a Two Word Name
def abbrev_name(name):
    names = name.split()

    first_initial = names[0][0]

    last_initial = names[-1][0]

    initials = first_initial.upper() + "." + last_initial.upper()
    return initials