
back = [[0]*3 for i in range(3)]
score = 15

things3 = [["r", 25], ["x", 20]]
things2 = sorted([["p", 15], ["a", 15], ["s", 20], ["c", 20]], key = lambda x: x[1], reverse=1)
things1 = sorted([["i", 100500], ["k", 15], ["t", 25], ["f", 15], ["d", 10]], key = lambda x: x[1], reverse=1)
score = 0

def place(r):
    global score
    max1 = things3[0][1]
    max2 = things2[0][1] + things1[0][1]
    max3 = sum([i[1] for i in things1][:2])
    if max1 > max2 and max1 > max3:
        back[r] = [things3[0][0]*3]
        things3.pop(0)
        score += max1
    elif max2 > max3:
        back[r][0] = things1[0][0]
        back[r][1] = things2[0][0]
        back[r][2] = things2[0][0]
        things1.pop(0)
        things2.pop(0)
        score += max2
    else:
        back[r][0] = things1[0][0]
        back[r][1] = things1[1][0]
        back[r][2] = things1[2][0]
        for j in range(3):
            things1.pop(0)
        score += max3



if __name__ == "__main__":
    for i in range(3):
        place(i)
    left1 = sum([i[1] for i in things1])
    left2 = sum([i[1] for i in things2])
    left3 = sum([i[1] for i in things3])
    score = score - 100500 + 5 - left1 - left2 - left3
    print(back, score)
