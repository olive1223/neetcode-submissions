class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        output = []
        curWordLength = 0
        curSentence = []
        def leftJustify():
            sentence = ''
            for sent in curSentence:
                sentence += sent + ' '
            remainingSpaces = maxWidth - len(sentence)
            if remainingSpaces >= 0:
                output.append(sentence + ' ' * remainingSpaces)
            else:
                output.append(sentence[:len(sentence)-1])
        
        for [index, word] in enumerate(words):
            curLength = curWordLength + len(curSentence) - 1 #num spaces
            #print(curLength, word, curWordLength)
            if len(word) + 1 + curLength > maxWidth:
                # word must go on next line
                if len(curSentence) == 1:
                    leftJustify()
                else:
                    remainingSpaces, uneven = divmod(maxWidth - curLength, len(curSentence)-1)
                    sentence = ''
                    #print(remainingSpaces, uneven)
                    for [i, sent] in enumerate(curSentence):
                        if i < len(curSentence) - 1:
                            sentence += sent + ' ' + ' ' * remainingSpaces
                            if i < uneven:
                                sentence += ' '
                        else:
                            sentence += sent
                    output.append(sentence)
                curWordLength = 0
                curSentence = []
            curSentence.append(word)
            curWordLength += len(word)
        
        # left justify last sentence
        leftJustify()
        return output

        
