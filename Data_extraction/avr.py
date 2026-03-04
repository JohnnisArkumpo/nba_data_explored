import statAverage

# File is for function and case:switch

texcade = "1950"

def cswitch(dcd):
    match dcd:
        case 50:
            texcade = "1950"
            return statAverage.st50
        case 60:
            texcade = "1960"
            return statAverage.st60
        case 70:
            texcade = "1970"
            return statAverage.st70
        case 80:
            texcade = "1980"
            return statAverage.st80
        case 90:
            texcade = "1990"
            return statAverage.st90
        case 00:
            texcade = "2000"
            return statAverage.st2k
        case 10:
            texcade = "2010"
            return statAverage.st2k10
        case 20:
            texcade = "2020"
            return statAverage.st2k20


# Function for finding the averages of decades.

def average(_decade):
    # cswitch(_decade)
    print(f"Choose all stat categories you would like to know the averages from texcade  (input: {_decade})")
