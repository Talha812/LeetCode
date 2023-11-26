class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        
        if "." in queryIP and ":" in queryIP:
            return "Neither"
        
        if "." in queryIP: #IPv4 Check
            segments = queryIP.split(".")
            if len(segments) != 4:
                return "Neither"
            for seg in segments:
                if seg.isdigit() and int(seg) <= 9:
                    if len(seg) == 1:
                        continue
                    else:
                        return "Neither"
                elif seg.isdigit() and int(seg) <= 99:
                    if len(seg) == 2:
                        continue
                    else:
                        return "Neither"
                elif seg.isdigit() and int(seg) <= 255:
                    continue
                else:
                    return "Neither"
            
            return "IPv4"
        
        elif ":" in queryIP: #IPv6 Check
            segments = queryIP.split(":")
            # print(segments)
            if len(segments) != 8:
                return "Neither"
            
            for seg in segments:
                if seg.isdigit():
                    if int(seg) == 0 and (len(seg) == 1 or len(seg) <= 4):
                        continue
                    elif int(seg) != 0 and len(seg) <= 4:
                        continue
                    else:
                        return "Neither"
                    
                elif len(seg) > 4:
                    return "Neither"
                
                else:
                    if len(seg) == 0:
                        return "Neither"
                    else:
                        for ch in seg:
                            if ch in "0123456789ABCDEFabcdef":
                                continue
                            else:
                                return "Neither"
                    
            return "IPv6"
        
        return "Neither"