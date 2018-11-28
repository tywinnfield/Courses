def donuts(count):
    if count < 10:
        return 'Number of donuts: %d' %count
    else:
        return 'Number of donuts: many'

print(donuts(1))




def both_ends(s):
    if len(s) > 2:
        return s[:2]+s[-2:] 
    else:
      return ""

print(both_ends("ete"))

def fix_start(s):
    first_char = s[0]
    modified_strg = s[1:].replace(first_char,"*")
    return print(first_char + modified_strg)
    

fix_start("barbababababa")

def mix_up(a, b):
    return b[0]+a[1:]+" "+a[0]+b[1:]

print(mix_up("jambon","fromage"))

def verbing(s):
    if len(s) >= 3:
        if s[-3:] == "ing":
            return s +"ly"
        else:
            return s +"ing"
    else:
        return s
print(verbing("beginning"))

