
localSentenceOnlyFinal = []
localPressOnlyFinalThree = []
localMixedPresFinalThree = []
localPressOnlyFinalTwo = []
localMixedPresFinalTwo = []
localPressOnlyFinalOne = []
localMixedPresFinalOne = []

with open('cleanLocalSentenceOnlyFinal.txt', 'r') as file1, open('cleanLocalPressOnlyFinalThree.txt', 'r') as file2, open(
        'cleanLocalMixedPresFinalThree.txt', 'r') as file3, open('cleanLocalPressOnlyFinalTwo.txt', 'r') as file4, open(
        'cleanLocalMixedPresFinalTwo.txt', 'r') as file5, open('cleanLocalPressOnlyFinalOne.txt', 'r') as file6, open(
        'cleanLocalMixedPresFinalOne.txt', 'r') as file7:

    localSentenceOnlyFinal = file1.readlines()

    localPressOnlyFinalThree = file2.readlines()

    localMixedPresFinalThree = file3.readlines()

    localPressOnlyFinalTwo = file4.readlines()

    localMixedPresFinalTwo = file5.readlines()

    localPressOnlyFinalOne = file6.readlines()

    localMixedPresFinalOne = file7.readlines()


# via this code, I learned at index 534, there is a mistake so afterwards the values are same at 2 index above between only sentence txt and others
"""
for i in range(2600):

    if localSentenceOnlyFinal[i][0] != localMixedPresFinalOne[i][1]:
        print(i)


"""

print(localSentenceOnlyFinal[533])
print(localMixedPresFinalOne[533])

print(localSentenceOnlyFinal[536])
print(localMixedPresFinalOne[534])



print(localSentenceOnlyFinal[2599])
print(localMixedPresFinalOne[2597])

j = 0


with open('fixed-cleanLocalSentenceOnlyFinal.txt', 'w') as file1, open('fixed-cleanLocalPressOnlyFinalThree.txt', 'w') as file2, open(
        'fixed-cleanLocalMixedPresFinalThree.txt', 'w') as file3, open('fixed-cleanLocalPressOnlyFinalTwo.txt', 'w') as file4, open(
        'fixed-cleanLocalMixedPresFinalTwo.txt', 'w') as file5, open('fixed-cleanLocalPressOnlyFinalOne.txt', 'w') as file6, open(
        'fixed-cleanLocalMixedPresFinalOne.txt', 'w') as file7:
    
    for i in range(2598):

        if i != 533:
            file1.write(localSentenceOnlyFinal[j])

            file2.write(localPressOnlyFinalThree[i])

            file3.write(localMixedPresFinalThree[i])

            file4.write(localPressOnlyFinalTwo[i])

            file5.write(localMixedPresFinalTwo[i])

            file6.write(localPressOnlyFinalOne[i])

            file7.write(localMixedPresFinalOne[i])

        if i == 533:
            j = 535

        j = j + 1

