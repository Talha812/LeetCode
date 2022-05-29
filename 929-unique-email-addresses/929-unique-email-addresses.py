class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        
        ans = set()
        
        for i in emails:
            splitted = i.split("@")
            localName = splitted[0]
            domainName = splitted[1]
            
            uni_local_name = ""
            for i in localName:
                if i == ".":
                    continue
                elif(i == "+"):
                    break
                else:
                    uni_local_name += i
            email = uni_local_name + "@" + domainName
            ans.add(email)
        
        return len(ans)
            
            