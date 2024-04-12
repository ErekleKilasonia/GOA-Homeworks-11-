#Growth of a Population
def nb_year(p0, percent, aug, p):
    num = p0
    years = 0
    while num < p:
        num = int(num + (num * (percent * 0.01)) + aug)
        years += 1
    return years
    