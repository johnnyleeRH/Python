import matplotlib.pyplot as plt

def showpic(timecost):
    plt.plot(range(0,len(timecost)), timecost)

    plt.savefig("/home/ssh001/timecost.jpg")

def showcost(file, pattern):
    f = open(file, 'r')
    cost = []
    while True:
        line = f.readline()
        if not line:
            break
        line = line.strip()
        if line.find(pattern) != -1:
            cost.append(float(line.split()[-2]))
            if cost[-1] > 100.0:
                print(len(cost), " ", cost[-1])
    f.close()
    #showpic(cost)
    print("total len ", len(cost))



if __name__ == '__main__':
    gfile = "/home/lrh/faw-ai-L4/data/log/prediction.log.20220303145044.record"
    pattern = "End to end time elapsed: "
    showcost(gfile, pattern)