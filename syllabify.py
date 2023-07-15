vowelSet = set("AEIOUaeiouÀÁÂÈÉÊÌÍÎÒÓÔÙÚÛàáâèéêìíîòóôùúû")
letterPairs = set(["bl", "br", "dr", "pl", "tr"])

def haveVowel(word):
    for let in word:
        if let in vowelSet:
            return True
    return False


def sliceValueInList(listSlice, valueSlice, indexSlice):
    result = listSlice[:]
    result.insert(valueSlice + 1, result[valueSlice][indexSlice:])
    result[valueSlice] = result[valueSlice][:indexSlice]
    return result


def mergeValueInList(listMerge, fromMerge, toMerge):
    result = listMerge[:]
    result[fromMerge : toMerge + 1] = ["".join(result[fromMerge : toMerge + 1])]
    return result


def syllabify(wordToSyllabify):
    word = wordToSyllabify

    # Break down word to constants and vowels. Ex: maglakad = ['m','a','gl','a','k','a','d']

    nextNg = False
    for letter in word:
        if letter in vowelSet:
            word = word.replace(letter, f" {letter} ")
        elif letter == "-":
            word = word.replace(letter, f" - ")
    word = word.replace("ng", "ŋ").replace("NG", "Ŋ")  # ng is temporarily replaced with ŋ so that it counts as one letter, hope its not some bullshit like 'Ng' or "nG"
    word = word.replace("'", "") # dont like apostrophes
    word = word.split()

    offset = 0

    for index, group in enumerate(word[:]):
        index += offset
        if index == 0 or index == len(word[:]) - 1 or word[index-1] == '-': # ignore at start or beginning of word, or if prev group was a hyphen
            continue
        elif len(group) == 2 and word: # if two letters, then split in half
            word = sliceValueInList(word[:], index, 1)
            offset += 1
        elif len(group) == 3:
            if (
                any((group[0].lower() == "n", group[0].lower() == "m"))
                and group[1:3].lower() in letterPairs
            ):  # if three letters and 1st letter is n/m and 2nd-3rd letter is bl, br, dr, pl, or tr, split n/m from letter pairs
                word = sliceValueInList(word[:], index, 1)
                offset += 1
            else: # if three letters and none of above rules apply, split first two letters from last letter
                word = sliceValueInList(word[:], index, 2)
                offset += 1
        elif len(group) > 3: # if four or more letters, detach first two letters
            word = sliceValueInList(word[:], index, 2)
            offset += 1

    # Join vowels with the constants that precede them

    joinWord = word[:]
    offset = 0
    for index, group in enumerate(joinWord):
        if (
            group[-1] in vowelSet
            and joinWord[index - 1] not in vowelSet
            and joinWord[index - 1] != "-"
            and index != 0
        ):
            word = mergeValueInList(word, index - 1 - offset, index - offset)
            offset += 1

    # Join vowels with the constants that follow them

    joinWord = word[:]
    offset = 0
    for index, group in enumerate(joinWord):
        if index != len(joinWord) - 1:
            if (
                group[-1] in vowelSet
                and not haveVowel(joinWord[index + 1])
                and joinWord[index + 1] != "-"
            ):
                word = mergeValueInList(word, index - offset, index + 1 - offset)
                offset += 1
    for i in range(len(word)):
        word[i] = word[i].replace("ŋ", "ng").replace("Ŋ", "NG")  # ŋ returns to ng

    while "-" in word: # bye bye hyphen
        word.remove("-")

    return word

print(syllabify("kumain"))
print(type(syllabify("kumain")))

