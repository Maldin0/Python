'''PSCP Program'''
def main(text, stats, graph, label):
    '''8349-VerticalHistogram 22/10/2022'''
    for i in text:
        stats[i] = 0
    for i in text:
        stats[i] += 1
    for i in range(1, max(stats.values())+1):
        label.append(str(i).zfill(3))
    for i in sorted(stats, key=str.swapcase):
        graph.append(str(i) + ('*' * stats[i]) + (' ' * (max(stats.values()) - stats[i])))
    for i, j in enumerate(reversed(label)):
        print(j, end=' ')
        for k in graph:
            print(k[::-1][i], end=' ')
        print()

main(input(), {}, [], ['   '])
