# class MagicDictionary(object):

#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.wordsdic={}

#     def buildDict(self, dict):
#         """
#         Build a dictionary through a list of words
#         :type dict: List[str]
#         :rtype: void
#         """
#         for i in dict:
#             self.wordsdic[len(i)]=self.wordsdic.get(len(i),[])+[i]

#     def search(self, word):
#         for candi in self.wordsdic.get(len(word),[]):
#                 countdiff=0
#                 for j in range(len(word)):
#                     if candi[j]!=word[j]:
#                         countdiff+=1
#                 if countdiff==1:
#                     return True
#         return False


class MagicDictionary(object):
    def __init__(self):
        self.wordsdict = {}
        
    def buildDict(self,Dict):
        for word in Dict:
            if len(word) not in self.wordsdict:
                self.wordsdict[len(word)] = [word]
            else:
                self.wordsdict[len(word)].append(word)
                     
    def search(self,word):
        if len(word) not in self.wordsdict: 
            return False
        else:
            count = 0
            for values in self.wordsdict[len(word)]:
                count = 0
                for i in range(len(values)):
                    if values[i] != word[i]:
                        count = count + 1
                if count == 1:
                    return True