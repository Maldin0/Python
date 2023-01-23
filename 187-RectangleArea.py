'''PSCP Program'''
def main(rec1, rec2):
    '''8353-RectangleArea 22/10/2022'''
    diffx = min(rec1[0] + rec1[2], rec2[0] + rec2[2]) - max(rec1[0], rec2[0])
    diffy = min(rec1[1] + rec1[3], rec2[1] + rec2[3]) - max(rec1[1], rec2[1])
    print(diffx * diffy if diffx >= 0 and diffy >= 0 else 'no overlapping')
main([int(i) for i in input().split()], [int(i) for i in input().split()])
