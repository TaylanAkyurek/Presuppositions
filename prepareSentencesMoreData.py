from datasets import load_from_disk
data = load_from_disk("eli5Dataset")



with open("sentencesMoreData.txt", "w") as file:
    for i in range(3600 * 4):
        line = data['train']['answers'][50000 + i]['text'][0]
        line = line.replace('\n', '')
        file.write(line)
        file.write("\n")
        print(i)

