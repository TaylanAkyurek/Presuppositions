

#prepare datasets that presupposition paragraph is below original paragraph:

bigSentenceOnlyFinal = []
bigPressOnlyFinalThree = []
bigMixedPresFinalThree = []
bigPressOnlyFinalTwo = []
bigMixedPresFinalTwo = []
bigPressOnlyFinalOne = []
bigMixedPresFinalOne = []


with open('big-cleanSentenceOnlyFinal.txt', 'r') as file1, open('big-cleanPressOnlyFinalThree.txt', 'r') as file2, open(
        'big-cleanMixedPresFinalThree.txt', 'r') as file3, open('big-cleanPressOnlyFinalTwo.txt', 'r') as file4, open(
        'big-cleanMixedPresFinalTwo.txt', 'r') as file5, open('big-cleanPressOnlyFinalOne.txt', 'r') as file6, open(
        'big-cleanMixedPresFinalOne.txt', 'r') as file7:

    bigSentenceOnlyFinal = file1.readlines()

    bigPressOnlyFinalThree = file2.readlines()

    bigMixedPresFinalThree = file3.readlines()

    bigPressOnlyFinalTwo = file4.readlines()

    bigMixedPresFinalTwo = file5.readlines()

    bigPressOnlyFinalOne = file6.readlines()

    bigMixedPresFinalOne = file7.readlines()

file1.close()
file2.close()
file3.close()
file4.close()
file5.close()
file6.close()
file7.close()

with open('big-presBelowSentenceOne.txt', 'w') as f1, open('big-presBelowSentenceTwo.txt', 'w') as f2, open(
        'big-presBelowSentenceThree.txt', 'w') as f3:
    for i in range(len(bigSentenceOnlyFinal)):

        f1.write(bigSentenceOnlyFinal[i])
        f1.write(bigPressOnlyFinalOne[i])

        f2.write(bigSentenceOnlyFinal[i])
        f2.write(bigPressOnlyFinalTwo[i])

        f3.write(bigSentenceOnlyFinal[i])
        f3.write(bigPressOnlyFinalThree[i])

f1.close()
f2.close()
f3.close()