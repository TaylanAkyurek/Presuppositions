def split_sentence(sentence):
    words = sentence.split()
    mid = len(words) // 2  # Using floor division
    first_half = ' '.join(words[:mid])
    second_half = ' '.join(words[mid:])
    return first_half, second_half

