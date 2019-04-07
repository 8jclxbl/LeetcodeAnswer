def longestWord(words):
    #set 可以进行排序
    words.sort()
    result = ''
    for word in words:
        if(len(word) >= len(result) and word<result):
            if all(word[:k] in words for k in range(1,len(word))) :
                result = word
 
    return result
#注意字符串可以直接进行比较

print(longestWord(["w","wo","wor","worl", "world","worldss",'worlds']))


