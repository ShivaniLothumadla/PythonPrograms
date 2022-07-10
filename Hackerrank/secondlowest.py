if __name__ == '__main__':
    names = []
    scores = []
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        names.append(name)
        scores.append(score)
        students.append([name, score])
    ss = set(sorted(scores))
    ss.remove(min(ss))
    sms = min(ss)
    sn = []
    for i in students:
        if i[1] == sms:
            sn.append(i[0])
    final_list = sorted(sn)
    for name in final_list:
        print(name)