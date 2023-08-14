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
    print(f'Word: {word}')
    # for j in word:
    #     print(f"J:{j}")
    #     if j[0] in ['a','e','i','o']:
    #         print(j[0])
    #         word.insert(word.index(j)+1,j[1:])
    #         word[word.index(j)] = word[word.index(j)][0]
    #     if len(j)>2:
    #         if j[:2]!='ng':
    #             word.insert(word.index(j) + 1, j[2:])
    #             word[word.index(j)] = word[word.index(j)][:2]

    return word


def checkConsonant(x):
    if (x == 'a' or x == 'e' or
            x == 'i' or x == 'o' or x == 'u'):
        return False
    else:
        return True

def translate(word:str):
    letra = {"a":["ᜀ"],"e":["ᜁ"],"i":["ᜁ"],"o":["ᜂ"],"u":["ᜂ"],"b": ["ᜊ᜔","ᜊ","ᜊᜒ","ᜊᜓ"],"k":["ᜃ᜔","ᜃ","ᜃᜒ","ᜃᜓ"],"d":["ᜇ᜔","ᜇ","ᜇᜒ","ᜇᜓ"],"g":["ᜄ᜔","ᜄ","ᜄᜒ","ᜄᜓ"],"h":["ᜑ᜔","ᜑ","ᜑᜒ","ᜑᜓ"],"l":["ᜎ᜔","ᜎ","ᜎᜒ","ᜎᜓ"],"m":["ᜋ᜔","ᜋ","ᜋᜒ","ᜋᜓ"],"n":["ᜈ᜔","ᜈ","ᜈ","ᜒᜈᜓ"],"ng":["ᜅ᜔","ᜅ","ᜅᜒ","ᜅᜓ"],"p":["ᜉ᜔","ᜉ","ᜉᜒ","ᜉᜓ"],"r":["ᜇ᜔","ᜇ","ᜇᜒ","ᜇᜓ"],"s":["ᜐ᜔","ᜐ","ᜐᜒ","ᜐᜓ"],"t":["ᜆ᜔","ᜆ","ᜆᜒ","ᜆᜓ"],"w":["ᜏ᜔","ᜏ","ᜏᜒ","ᜏᜓ"],"y": ["ᜌ᜔","ᜌ","ᜌᜒ","ᜌᜓ"]}
    word = syllabify(word)
    baybayin=""
    for pantig in word:
        if len(pantig)>2:
            if checkConsonant(pantig[0]) is True:
                if checkConsonant(pantig[1]) is True:
                    word.insert(word.index(pantig), pantig[0])
                    word[word.index(pantig)] = word[word.index(pantig)][1:3]
                else:
                    word.insert(word.index(pantig) + 1, pantig[2:])
                    word[word.index(pantig)] = word[word.index(pantig)][:2]
    for pantig in word:
        if pantig[0] in ['a', 'b', 'k', 'd', 'e', 'i', 'g', 'h', 'l', 'm', 'n', 'ng', 'p', 'r', 's', 't', 'o', 'u', 'w','y']:
            if len(pantig) < 2:
                baybayin+=letra[pantig][0]
            else:
                j = pantig[1]
                if pantig[:2] == 'ng':
                    j = pantig[2]
                if j == 'a':
                    baybayin+=letra[pantig[0]][1]
                if j in ['e', 'i']:
                    baybayin+=letra[pantig[0]][2]
                if j in ['o', 'u']:
                    baybayin+=letra[pantig[0]][3]
        else:
            baybayin=f"The letter {pantig[0]} is not in the Tagalog alphabet. Before transcripting a word to Baybayin, please make sure to translate the word to Tagalog first."
    return baybayin

# #test on: bakit, basta
#z=translate('nakakapagpabagabag')
z=translate('lunes')
print(z)