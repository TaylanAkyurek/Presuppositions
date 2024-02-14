import nltk

from datasets import load_dataset
from datasets import load_from_disk

import openai
openai.api_key = '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'

sentence = "The opinions expressed by columnists are their own and do not represent the views of Townhall.com."
input_text = "I want you to generate a presupposition of the sentence indicated by angel brackets. The sentence I want you to generate presupposition is: <" + sentence + ">. Also, presupposition you generated must be significantly DIFFERENT from original sentence which is: " + sentence +", THAT IS REALLY IMPORTANT."

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]
def getPress(sentence):
  prompt = f"""  input_text = "I want you to generate 3 presupposition of the sentence indicated by angel brackets.\
  The sentence I want you to generate presupposition is: <{sentence}>.\ 
  Also, presupposition you generated must be significantly different from original sentence.
  I lastly want you to chose these presuppositions in order to give best information about the world or situation that my sentence in angel brackets occured.\
  Also, just seperate your 3 presupposition with a space and write them, do not enumarete them or start to a new line.\
  For example if the sentence is:  'The CEO resigned after the scandal,' , I want an output like: 'There was a scandal. The person in question was the CEO. The CEO’s resignation was a result of the scandal'\
  Now, generate me 3 presuppositions of the sentence indicated by angel brackets, based on guidelines above. I want to remind you the sentence:  <{sentence}>.\ 
    """
  return get_completion(prompt)

print(getPress(sentence))


"""
rw = load_dataset("tiiuae/falcon-refinedweb")

data = rw['content'].select(range(20000))

data.save_to_disk("falcon-refinedwebDataset")
"""

data = load_from_disk("eli5Dataset")

# print(eli5['train']['answers'][10]['text'][0])

# text = eli5['train']['answers']['text'][0].select(range(10))

nltk.download('punkt')

presuppositionStr = ""  # threePress
originalLine = ""

presAndSentence = ""

onePres = ""
onePresAndSentence = ""

twoPres = ""
twoPresAndSentence = ""

with open('middle-sentenceOnlyFinal.txt', 'w') as file1, open('middle-presBelowSentenceOne.txt', 'w') as file2, open(
        'middle-presBelowSentenceTwo.txt', 'w') as file3, open('middle-presBelowSentenceThree.txt', 'w') as file4, open(
        'middle-mixedPresFinalOne.txt', 'w') as file5, open('middle-pressOnlyFinalTwo.txt', 'w') as file6, open(
        'middle-mixedPresFinalThree.txt', 'w') as file7:
    for i in range(1000):

        line = data['train']['answers'][5000 + i]['text'][0]
        sentences = nltk.sent_tokenize(line)

        presuppositionStr = ""
        presAndSentence = ""

        onePres = ""
        onePresAndSentence = ""

        twoPres = ""
        twoPresAndSentence = ""

        for sentence in sentences:

            try:
                presuppositions = getPress(sentence)
                presArray = nltk.sent_tokenize(presuppositions)
                presuppositionStr = presuppositionStr + " " + presuppositions
                presAndSentence = presAndSentence + " " + sentence + " " + presuppositions

                try:
                    onePres = onePres + " " + presArray[0]
                    twoPres = twoPres + " " + presArray[0] + " " + presArray[1]

                    onePresAndSentence = onePresAndSentence + " " + sentence + " " + presArray[0]
                    twoPresAndSentence = twoPresAndSentence + " " + sentence + " " + presArray[0] + " " + presArray[1]
                except:
                    print("indexing error")



            except:
                presuppositions = sentence
                onePres = onePres + " " + sentence
                twoPres = twoPres + " " + sentence
                presuppositionStr = presuppositionStr + " " + sentence
                onePresAndSentence = onePresAndSentence + " " + sentence
                twoPresAndSentence = twoPresAndSentence + " " + sentence
                presAndSentence = presAndSentence + " " + sentence
                print("missed")

        presuppositionStr = presuppositionStr.replace('\n', '')
        line = line.replace('\n', '')
        presAndSentence = presAndSentence.replace('\n', '')

        onePres = onePres.replace('\n', '')
        twoPres = twoPres.replace('\n', '')
        onePresAndSentence = onePresAndSentence.replace('\n', '')
        twoPresAndSentence = twoPresAndSentence.replace('\n', '')

        file1.write(line)
        file1.write("\n")

        file2.write(line)
        file2.write("\n")
        file2.write(onePres)
        file2.write("\n")

        file3.write(line)
        file3.write("\n")
        file3.write(twoPres)
        file3.write("\n")

        file4.write(line)
        file4.write("\n")
        file4.write(presuppositionStr)
        file4.write("\n")

        file5.write(onePresAndSentence)
        file5.write("\n")

        file6.write(twoPresAndSentence)
        file6.write("\n")

        file7.write(presAndSentence)
        file7.write("\n")

        print("sentence:", line)
        print("")
        print("presuppositions:", presuppositionStr)
        print("")
        print("presAndSentence:", presAndSentence)
        print("")

        print("onePres:", onePres)
        print("")
        print("onePresAndSentence:", onePresAndSentence)
        print("")
        print("twoPres:", twoPres)
        print("")
        print("twoPresAndSentence:", twoPresAndSentence)

        print(i)

file1.close()
file2.close()
file3.close()
file4.close()
file5.close()
file6.close()
file7.close()

"""
with open('presuppositionsOpenwebBackup.txt', 'w') as fff:
    for data in updatedSentencesWhole:
        line = data
        ff.write(line)
        ff.write('\n')
ff.close()
"""
