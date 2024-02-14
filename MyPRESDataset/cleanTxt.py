
localSentenceOnlyFinal = []
localPressOnlyFinalThree = []
localMixedPresFinalThree = []
localPressOnlyFinalTwo = []
localMixedPresFinalTwo = []
localPressOnlyFinalOne = []
localMixedPresFinalOne = []

with open('sentenceOnlyFinal.txt', 'r') as file1, open('pressOnlyFinalThree.txt', 'r') as file2, open(
        'mixedPresFinalThree.txt', 'r') as file3, open('pressOnlyFinalTwo.txt', 'r') as file4, open(
        'mixedPresFinalTwo.txt', 'r') as file5, open('pressOnlyFinalOne.txt', 'r') as file6, open(
        'mixedPresFinalOne.txt', 'r') as file7:

        localSentenceOnlyFinal = file1.readlines()

        localPressOnlyFinalThree = file2.readlines()

        localMixedPresFinalThree = file3.readlines()

        localPressOnlyFinalTwo = file4.readlines()

        localMixedPresFinalTwo = file5.readlines()

        localPressOnlyFinalOne = file6.readlines()

        localMixedPresFinalOne = file7.readlines()



print(len(localSentenceOnlyFinal))
print(len(localPressOnlyFinalThree))
print(len(localMixedPresFinalThree))
print(len(localPressOnlyFinalTwo))
print(len(localMixedPresFinalTwo))
print(len(localPressOnlyFinalOne))
print(len(localMixedPresFinalOne))




with open('cleanSentenceOnlyFinal.txt', 'w') as file1, open('cleanPressOnlyFinalThree.txt', 'w') as file2, open(
        'cleanMixedPresFinalThree.txt', 'w') as file3, open('cleanPressOnlyFinalTwo.txt', 'w') as file4, open(
        'cleanMixedPresFinalTwo.txt', 'w') as file5, open('cleanPressOnlyFinalOne.txt', 'w') as file6, open(
        'cleanMixedPresFinalOne.txt', 'w') as file7:
        for i in range(1000):

                file1.write(localSentenceOnlyFinal[i])

                file2.write(localPressOnlyFinalThree[i])

                file3.write(localMixedPresFinalThree[i])

                file4.write(localPressOnlyFinalTwo[i])

                file5.write(localMixedPresFinalTwo[i])

                file6.write(localPressOnlyFinalOne[i])

                file7.write(localMixedPresFinalOne[i])
