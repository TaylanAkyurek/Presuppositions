localSentenceOnlyFinal = []
localPressOnlyFinalThree = []
localMixedPresFinalThree = []
localPressOnlyFinalTwo = []
localMixedPresFinalTwo = []
localPressOnlyFinalOne = []
localMixedPresFinalOne = []
with open('fixed-cleanLocalSentenceOnlyFinal.txt', 'r') as file1, open('fixed-cleanLocalPressOnlyFinalThree.txt', 'r') as file2, open(
        'fixed-cleanLocalMixedPresFinalThree.txt', 'r') as file3, open('fixed-cleanLocalPressOnlyFinalTwo.txt', 'r') as file4, open(
        'fixed-cleanLocalMixedPresFinalTwo.txt', 'r') as file5, open('fixed-cleanLocalPressOnlyFinalOne.txt', 'r') as file6, open(
        'fixed-cleanLocalMixedPresFinalOne.txt', 'r') as file7:

    localSentenceOnlyFinal = file1.readlines()

    localPressOnlyFinalThree = file2.readlines()

    localMixedPresFinalThree = file3.readlines()

    localPressOnlyFinalTwo = file4.readlines()

    localMixedPresFinalTwo = file5.readlines()

    localPressOnlyFinalOne = file6.readlines()

    localMixedPresFinalOne = file7.readlines()

file1.close()
file2.close()
file3.close()
file4.close()
file5.close()
file6.close()
file7.close()


sentenceOnlyFinal = []
pressOnlyFinalThree = []
mixedPresFinalThree = []
pressOnlyFinalTwo = []
mixedPresFinalTwo = []
pressOnlyFinalOne = []
mixedPresFinalOne = []

with open('cleanSentenceOnlyFinal.txt', 'r') as f1, open('cleanPressOnlyFinalThree.txt', 'r') as f2, open(
        'cleanMixedPresFinalThree.txt', 'r') as f3, open('cleanPressOnlyFinalTwo.txt', 'r') as f4, open(
        'cleanMixedPresFinalTwo.txt', 'r') as f5, open('cleanPressOnlyFinalOne.txt', 'r') as f6, open(
        'cleanMixedPresFinalOne.txt', 'r') as f7:

    sentenceOnlyFinal = f1.readlines()

    pressOnlyFinalThree = f2.readlines()

    mixedPresFinalThree = f3.readlines()

    pressOnlyFinalTwo = f4.readlines()

    mixedPresFinalTwo = f5.readlines()

    pressOnlyFinalOne = f6.readlines()

    mixedPresFinalOne = f7.readlines()

f1.close()
f2.close()
f3.close()
f4.close()
f5.close()
f6.close()
f7.close()



bigSentenceOnlyFinal = sentenceOnlyFinal + localSentenceOnlyFinal
bigPressOnlyFinalThree = pressOnlyFinalThree + localPressOnlyFinalThree
bigMixedPresFinalThree = mixedPresFinalThree + localMixedPresFinalThree
bigPressOnlyFinalTwo = pressOnlyFinalTwo + localPressOnlyFinalTwo
bigMixedPresFinalTwo = mixedPresFinalTwo + localMixedPresFinalTwo
bigPressOnlyFinalOne = pressOnlyFinalOne + localPressOnlyFinalOne
bigMixedPresFinalOne = mixedPresFinalOne + localMixedPresFinalOne


print(len(bigSentenceOnlyFinal))
print(len(bigPressOnlyFinalThree))
print(len(bigMixedPresFinalThree))
print(len(bigPressOnlyFinalTwo))
print(len(bigMixedPresFinalTwo))
print(len(bigPressOnlyFinalOne))
print(len(bigMixedPresFinalOne))

print(bigSentenceOnlyFinal[10])
print(bigPressOnlyFinalThree[10])
print(bigMixedPresFinalThree[10])
print(bigPressOnlyFinalTwo[10])
print(bigMixedPresFinalTwo[10])
print(bigPressOnlyFinalOne[10])
print(bigMixedPresFinalOne[10])



print(bigSentenceOnlyFinal[533])
print(bigPressOnlyFinalThree[533])
print(bigMixedPresFinalThree[533])
print(bigPressOnlyFinalTwo[533])
print(bigMixedPresFinalTwo[533])
print(bigPressOnlyFinalOne[533])
print(bigMixedPresFinalOne[533])

print(bigSentenceOnlyFinal[2000])
print(bigPressOnlyFinalThree[2000])
print(bigMixedPresFinalThree[2000])
print(bigPressOnlyFinalTwo[2000])
print(bigMixedPresFinalTwo[2000])
print(bigPressOnlyFinalOne[2000])
print(bigMixedPresFinalOne[2000])

print(bigSentenceOnlyFinal[3000])
print(bigPressOnlyFinalThree[3000])
print(bigMixedPresFinalThree[3000])
print(bigPressOnlyFinalTwo[3000])
print(bigMixedPresFinalTwo[3000])
print(bigPressOnlyFinalOne[3000])
print(bigMixedPresFinalOne[3000])

with open('big-cleanSentenceOnlyFinal.txt', 'w') as ff1, open('big-cleanPressOnlyFinalThree.txt', 'w') as ff2, open(
        'big-cleanMixedPresFinalThree.txt', 'w') as ff3, open('big-cleanPressOnlyFinalTwo.txt', 'w') as ff4, open(
        'big-cleanMixedPresFinalTwo.txt', 'w') as ff5, open('big-cleanPressOnlyFinalOne.txt', 'w') as ff6, open(
        'big-cleanMixedPresFinalOne.txt', 'w') as ff7:
    for i in range(len(bigSentenceOnlyFinal)):

        ff1.write(bigSentenceOnlyFinal[i])

        ff2.write(bigPressOnlyFinalThree[i])

        ff3.write(bigMixedPresFinalThree[i])

        ff4.write(bigPressOnlyFinalTwo[i])

        ff5.write(bigMixedPresFinalTwo[i])

        ff6.write(bigPressOnlyFinalOne[i])

        ff7.write(bigMixedPresFinalOne[i])

ff1.close()
ff2.close()
ff3.close()
ff4.close()
ff5.close()
ff6.close()
ff7.close()
