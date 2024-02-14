from datasets import load_from_disk
data = load_from_disk("eli5Dataset")



with open("testData.txt", "w") as file:
    for i in range(800):
        line = data['test']['answers'][i]['text'][0]
        line = line.replace('\n', '')

        file.write(line)
        file.write("\n")
        print(i)

