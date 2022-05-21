class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        
        temp = score.copy()
        if(len(temp) <= 3):
            ans = [""]*len(score)

            dic = {}
            grade = 1
            while(len(temp) != 0):
                max_num = max(temp)
                dic[max_num] = str(grade)
                grade += 1
                temp.remove(max_num)

            for s in range(len(score)):
                if(dic[score[s]] == "1"):
                    ans[s] = "Gold Medal"
                elif(dic[score[s]] == "2"):
                    ans[s] = "Silver Medal"
                elif(dic[score[s]] == "3"):
                    ans[s] = "Bronze Medal"
                    
            return ans
        
        if(len(temp) > 3):
            first_score = max(temp)
            temp.remove(first_score)

            sec_score = max(temp)
            temp.remove(sec_score)

            third_score = max(temp)
            temp.remove(third_score)

            ans = [""]*len(score)

            dic = {}
            grade = 4
            while(len(temp) != 0):
                max_num = max(temp)
                dic[max_num] = str(grade)
                grade += 1
                temp.remove(max_num)

            for s in range(len(score)):
                if(score[s] == first_score):
                    ans[s] = "Gold Medal"
                elif(score[s] == sec_score):
                    ans[s] = "Silver Medal"
                elif(score[s] == third_score):
                    ans[s] = "Bronze Medal"
                else:
                    ans[s] = dic[score[s]]

            return ans
        