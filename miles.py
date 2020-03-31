from datetime import date
from datetime import timedelta


dayStart = date(2019, 1, 1)
dayEnd = date(2019, 12, 27)
daysDiff = dayEnd - dayStart
totalDays = (dayEnd - dayStart).days
earnedIncome = 9404.0
totalDays = (24.0 - 6.0)/24.0*totalDays  # totalDays not sleeping
daysWorkedFactor = (5.0/7.0)  # 5 days out of 7 days working
daysPerTank = 1.5
daysPerMonth = 31
milesPerTank = 300
commuteMilesPerDay = 70
totalMonth = 9
daysWorked = totalDays * daysWorkedFactor
personalDays = totalDays - daysWorked
# compute milage
milesPerDay = milesPerTank / daysPerTank
milage = milesPerDay * daysWorked
personalMilage = milesPerDay * personalDays
commuteMilage = commuteMilesPerDay * daysWorked
milageWorked = milage - commuteMilage
workedFactor = 0.58
deduct = milageWorked * workedFactor
print("day delta: {}".format(daysDiff.days))
print("days worked: {}".format(daysWorked))
print("personal days: {}".format(personalDays))
print("milage: {} = {} * {}".format(milage, milesPerDay, daysWorked))
print("personal milage: {} = {} * {}".format(personalMilage,
                                        milesPerDay, personalDays))
print("commuteMilage: {} = {} * {}".format(commuteMilage,
                                    commuteMilesPerDay, daysWorked))
print("milageWorked: {} = {} - {}".format(milageWorked, milage, commuteMilage))
print("total milage: {}".format(milesPerDay * (daysWorked + personalDays)))

print("Deductible is: {}".format(deduct))
print("Earned - Deduct: {}".format(earnedIncome - deduct))

rentStart = date(2019, 1, 1)
rentEnd = date(2019, 9, 1)
personalEnd = date(2019, 12, 31)
print("Rental days was: {}".format((rentEnd - rentStart).days))
print("Personal days was: {}".format((personalEnd - rentEnd)))

total = personalEnd - rentStart
year = timedelta(days=365)
proportion = total.days / year.days
month = 12*proportion
print("month total: {}".format(month))
print("hoa: {}".format(month*210.0))