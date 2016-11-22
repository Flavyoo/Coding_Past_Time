import random
#In 1693 Samuel Pepys asked Isaac Newton which is more likely:
#getting 1 at least once when rolling a fair die six times or
#getting 1 at least twice when rolling it 12 times. Compose a
#program that could have provided Newton with a quick answer.

def sixLike():
    six_count = 0
    ave1 = 0
    for j in range(100):
        for i in range(6):
            a = random.randrange(7)
            if a == 1:
                six_count += 1
        aa = six_count / 6
        ave1 += aa
    return ave1 / 100;

def twelveLike():
    twelve_count = 0
    ave2 = 0
    for j in range(100):
        for i in range(13):
            b = random.randrange(13)
            if b == 1:
                twelve_count+= 1
        bb = twelve_count / 12
        ave2 += bb
    return ave2 / 100;

ma = max(sixLike(), twelveLike())
mi = min(sixLike(), twelveLike())
if ma == sixLike():
    stdio.writeln()
    print "{0:.2f}: Rolling a die six times and getting one at least once\
 is more likely.\n\n".format(ma)
else:
    stdio.writeln()
    print "{0:.2f}: Rolling a die 12 times and getting one at least twice\
 is more likely\n\n".format(mi)
