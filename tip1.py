bill = float(raw_input("What was the total bill amount? "))
service = raw_input("Was the level of service: good, fair, bad? ")
print "Total bill amount? %.2f" % bill
print "Level of service? %s" % service

if (service == "good"):
    tip = bill * .20
    total = tip + bill
    print "Tip amount: %.2f" % tip
    print "Total amount: %.2f" % total

elif (service == "fair"):
    tip = bill * .15
    total = tip + bill
    print "Tip amount: %.2f" % tip
    print "Total amount: %.2f" % total

elif (service == "bad"):
    tip = bill * .10
    total = tip + bill
    print "Tip amount: %.2f" % tip
    print "Total amount: %.2f" % total
