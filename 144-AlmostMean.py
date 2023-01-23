'''PSCP Program'''


def main():
    '''AlmostMean'''
    data = []
    id_num = []
    for _ in range(int(input())):
        line = input()
        data.append(float(line[line.find("	")+1:]))
        id_num.append(line[:line.find("	")])
    average = sum(data)/len(data)
    sorted_data = sorted(data, reverse=True)
    for i in sorted_data:
        if i < average:
            print(id_num[data.index(i)], i, sep='\t')
            break

main()
