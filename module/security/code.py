import random
def make_code(in_len: int) -> str:
    try:
        result = ""
        down_case = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        upper_case = ["A", "B", "C", "D", "E", "F", "G", "H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        numbers = [0,1,2,3,4,5,6,7,8,9]
        while len(result) <= in_len-1:
            big = random.randint(0,2)
            if big == 0:
                res = down_case[random.randint(0,len(down_case)-1)]
                result += res
            elif big == 1:
                res = upper_case[random.randint(0,len(upper_case)-1)]
                result += res
            else:
                res = numbers[random.randint(0,len(numbers)-1)]
                result += str(res)
        return result
    except:
        return 'error'