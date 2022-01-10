def count_substring(string, sub_string):
    count = 0
    for i in range(len(string)):
        if string[i] == sub_string[0]:
            if(len(string)-1 == i):
                continue
            else:
                find = string[i:i+len(sub_string)]
                if(find == sub_string):
                    count +=1
    
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)