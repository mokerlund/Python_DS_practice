#What is the chance that B will occur given A?
#Two tests were given, for Test A, 80% passed. For Test B, 60% passed.
# What is the percentage of students that passed both?
#P(B|A) = P(A,B)=60/P(A)=80 == 75%

from numpy import random
random.seed(0)

totals = {20:0, 30:0, 40:0, 50:0, 60:0, 70:0}
purchases = {20:0, 30:0, 40:0, 50:0, 60:0, 70:0}
total_purchases = 0
for i in range(100000):
    age_decade = random.choice([20, 30, 40, 50, 60, 70])
    purchase_probability = float(age_decade) / 100.0
    totals[age_decade] += 1
    if (random.random() < purchase_probability):
        total_purchases += 1
        purchases[age_decade] += 1

totals
purchases
total_purchases

#Let's play with conditional probability

#Computing P(E|F) where E is "purchase" and F is "you're in your 30s".
PEF = float(purchases[30]) / float(totals[30])
print("P(purchase | 30s): ", PEF)

#Computing probability of F P(F) = Probability of someone being in their 30s.
PF = float(totals[30]) / 100000.0
print("P(30s): ", PF)

#Computing probability of E P(E) = Probablility of someone buying something.
PE = float(total_purchases) / 100000.0
print("P(purchase): ", PE)

#If E and F were independent, then we would expect them to be the same.

#Compute P(E)*P(F)
print("P(30s)*P(Purchase)", PE * PF)

#P(E,F) is the probability of being 30 and buying something out of the
#whole population, not just out of the 30s, which is P(E|F)
print("P(30's, Purchase", float(purchases[30]) / 100000.0)

#P(E,F) = P(E)*P(F) is close in this situation, but because they are dependent on each other
#and the randomness of the data, it's not quite the same.

#We can still check that P(E|F) = P(E,F)*P(F)
print("P(E|F)", float(purchases[30]/100000.0) / PF)

#Assignment - Change the code such that the purchase probability does not vary with age.
#Then confirm that P(E|F) is about the same as P(E)

totals = {20:0, 30:0, 40:0, 50:0, 60:0, 70:0}
purchases = {20:0, 30:0, 40:0, 50:0, 60:0, 70:0}
total_purchases = 0
for i in range(100000):
    age_decade = random.choice([20, 30, 40, 50, 60, 70])
    purchase_probability = 40.00 / 100.0
    totals[age_decade] += 1
    if (random.random() < purchase_probability):
        total_purchases += 1
        purchases[age_decade] += 1

PEF = float(purchases[30]) / float(totals[30])
PE = float(total_purchases) / 100000.0

PEF
PE