bill = float(raw_input("What was the total bill amount? "))
service = raw_input("Was the level of service: Good, Fair, Bad? ")
split = int(raw_input("Split how many ways? "))
service = service.upper()

print "Total bill amount? %.2f" % bill
print "Level of service? %s" % service
print "Split how many ways %d" % split

if (service == "GOOD"):
    tip = bill * .20
    total = tip + bill
    split_per = total / split
    print "Tip amount: %.2f" % tip
    print "Total amount: %.2f" % total
    print "Amount per person: %.2f" % split_per

elif (service == "FAIR"):
    tip = bill * .15
    total = tip + bill
    split_per = total / split
    print "Tip amount: %.2f" % tip
    print "Total amount: %.2f" % total
    print "Amount per person: %.2f" % split_per

elif (service == "BAD"):
    tip = bill * .10
    total = tip + bill
    split_per = total / split
    print "Tip amount: %.2f" % tip
    print "Total amount: %.2f" % total
    print "Amount per person: %.2f" % split_per
