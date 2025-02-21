import random
def randomMonthGer():
    randomMonthLogin = {
        1: "Januar",
        2: "Februar",
        3: "März",
        4: "April",
        5: "Mai",
        6: "Juni",
        7: "Juli",
        8: "August",
        9: "September",
        10: "Oktober",
        11: "November",
        12: "Dezember"
        }
    return randomMonthLogin[random.randint(1,12)]

def randomMonthEng():
    randomMonthLogin = {
        1: "January",  
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
        }
    return randomMonthLogin[random.randint(1,12)]