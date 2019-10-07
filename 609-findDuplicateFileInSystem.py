class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        files = {}
        greaterOne = set()
        for i in paths:
            temp = i.split()
            for j in temp[1:]:
                fileName,fileContent = j.split('(')
                fileContent = fileContent[:-1]
                completePath = temp[0] + '/' + fileName
                if fileContent in files:
                    files[fileContent].append(completePath)
                    greaterOne.add(fileContent)
                else:
                    files[fileContent] = [completePath]
        res = []
        for i in greaterOne:
            res.append(files[i])
        return res