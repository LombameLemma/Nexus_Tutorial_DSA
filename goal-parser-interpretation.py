class Solution:
    def interpret(self, command: str) -> str:
        c=[]
        for i in range (0,len(command)):
            if command[i] == "G":
                c.append("G")
                i+=1
            elif command[i:i+2] == "()":
                c.append("o")
                i+=2
            elif command[i:i+4] == "(al)":
                c.append("al")
                i+=4
        print(c)
        return "".join(c)  
