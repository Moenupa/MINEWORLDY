
def judge():
    '''
    code for Q002 -- testing --
    '''
    yn_list = []
    for i in range(int(input())):
        mates = int(input())
        flag, count = False, 0
        for j in range(mates):
            person = input()
            flag |= person == "COMP 2020"
            count += 2021 - int(person[-4:])
        yn_list.append("YES" if 0 < mates <= 3 and flag == True and count <= 5 else "NO")

    print('\n'.join(yn_list))

def judge3():
    '''
    code for Q003 -- testing --
    '''
    result = []
    for i in range(int(input())):
        sample = [int(j) for j in input().split(" ")]
        if (sample[0] - 1) % (sample[1] + 1) == 0:
            result.append("Piiiiiiiiiiiiiii")
        else:
            result.append("Wuhoo")

    print("\n".join(result))

def judge4():
    '''
    code for Q004 -- testing --
    '''
    history = {}

    for i in range(int(input())):
        cur_member = input().replace(" ","")
        if i == 0:
            try:
                history[cur_member] += 1
            except KeyError:
                history[cur_member] = 1
            continue

        for past_member in history.keys():
            if int(cur_member[0]) > int(past_member[0]) and int(cur_member[1]) > int(past_member[1]) and int(cur_member[2]) > int(past_member[2]):
                history[past_member] = 0
        
        if i != 0:
            try:
                history[cur_member] += 1
            except KeyError:
                history[cur_member] = 1
    print(sum(history.values()))

if __name__ == "__main__":
    judge4()