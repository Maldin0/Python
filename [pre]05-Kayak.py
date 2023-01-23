"""I hate Kayak"""
def main():
    """Please make this end"""
    _ = int(input())
    weight = input().split()
    weight = [int(i) for i in weight]#เปลี่ยนทุกตัวในlist เป็น int
    weight.sort()#เรียงใหม่
    sumofdif = 0
    while len(weight) != 2:#ทำจนกว่าจะเหลือ2ตัวสุดท้าย
        for i in range(len(weight)-1):#วนลูปที่-1เพราะไม่เทียบกับตัวเอง
            if i == 0:#ครั้งแรก
                mindiff = weight[i+1]-weight[i]
                newdiff = mindiff+1
                numx = i
            else:#ครั้งต่อๆมา
                newdiff = weight[i+1]-weight[i]
            if  mindiff > newdiff:#เช็คว่าอันไหนน้อยสุด
                mindiff = newdiff
                numx = i
        sumofdif += mindiff#ผลรวมผลต่าง
        weight.pop(int(numx))#เอาตัวที่ใช้แล้วออก
        weight.pop(int(numx))#เอาตัวที่ใช้แล้วออก
    print(sumofdif)
main()
