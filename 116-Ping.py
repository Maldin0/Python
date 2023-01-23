'''Huh wtf is this'''


def main():
    '''Ping.exe'''
    _, _ = input(), input()  # Useless information get sent to the void
    ip_addr = input()
    ping_time, out, recieve = [input(), input(), input(), input()], '', 0
    ip_addr = get_ip_address(ip_addr)
    for k in range(4):
        loc_1, loc_2 = None, None
        temp = ping_time[k].replace('bytes=32', '').replace('Reply from', '')
        if temp == 'General failure.' or temp == 'Request timed out.':
            out += '0'
        else:
            for i, j in enumerate(temp):
                if j == '=':
                    loc_1 = i+1
                elif j == '<':
                    loc_1 = i
                elif j == 's':
                    loc_2 = i-1
                    out += temp[loc_1:loc_2] + ' '
                    recieve += 1
                    break
    data_out = ping_reading(out)
    low_p = data_out[0]
    high_p = data_out[1]
    if data_out[0] is None:
        low_p = data_out[3]
    if data_out[1] is None:
        high_p = data_out[3]
    ping_report(ip_addr=ip_addr,
                avg=data_out[2], mini=low_p, maxi=high_p, recieve=recieve)


def get_ip_address(ip_addr):
    '''Decypher ip address from ping.exe'''
    hexa, loc_1, loc_2 = ('ABCDEF0123456789'), 0, 0
    copy_ip_addr = ip_addr
    for i, j in enumerate(ip_addr):
        if i > 7 and j == '[':
            loc_1 = i
        elif j == ']':
            loc_2 = i
            break
    ip_addr = ip_addr[loc_1+1:loc_2]
    if len(ip_addr) < 7:
        for i, j in enumerate(copy_ip_addr):
            if i == 8 and j in hexa:
                loc_1 = i
            elif j == 'w':
                loc_2 = i-1
                break
        ip_addr = copy_ip_addr[loc_1:loc_2]
    return ip_addr


def get_top_ping(buffer, ping, count, average, stats):
    '''return lowest avg and highest ping'''
    ping1, ping2, ping3, ping4 = ping[0], ping[1], ping[2], ping[3]
    highest, lowest = stats[0], stats[1]
    if buffer == '<1':
        buffer = 0
    average += int(buffer)
    count += 1
    if ping1 is None:
        ping1 = int(buffer)
    elif ping2 is None:
        ping2 = int(buffer)
        if ping1 > ping2:
            highest, lowest = ping1, ping2
        else:
            highest, lowest = ping2, ping1
    elif ping3 is None:
        ping3 = int(buffer)
        if ping3 > highest:
            highest = ping3
        elif ping3 < lowest:
            lowest = ping3
    elif ping4 is None:
        ping4 = float(buffer)
        if ping4 > highest:
            highest = ping4
        elif ping4 < lowest:
            lowest = ping4
    return lowest, highest, average, count, ping1, ping2, ping3, ping4


def ping_reading(out):
    '''Get ping statistics'''
    average, count, buffer, highest, lowest = 0, 0, '', None, None
    ping1, ping2, ping3, ping4 = None, None, None, None
    for j in out:
        if j.isnumeric() or j == '<':
            buffer += j
        if j == ' ':
            ping, stats = (ping1, ping2, ping3, ping4), (highest, lowest)
            temp_data_out = get_top_ping(buffer, ping, count, average, stats)
            average, count = temp_data_out[2], temp_data_out[3]
            ping1, ping2 = temp_data_out[4], temp_data_out[5]
            ping3, ping4 = temp_data_out[6], temp_data_out[7]
            lowest, highest = temp_data_out[0], temp_data_out[1]
            buffer = ''
    if count != 0:
        average = average // count
    else:
        average = 0
    return lowest, highest, average, ping1


def ping_report(ip_addr, recieve, avg, mini, maxi):
    '''Report'''
    print('Ping statistics for %s:' % ip_addr)
    print('    Packets: Sent = 4, Received = ', end='')
    print('%d, Lost = %d (%d%% loss),' %
          (recieve, 4-recieve, (abs(recieve-4)/4)*100))
    if (abs(recieve-4)/4)*100 != 100:
        print('Approximate round trip times in milli-seconds:')
        print('    Minimum = %dms, Maximum = %dms, Average = %dms' %
              (mini, maxi, avg))


main()
