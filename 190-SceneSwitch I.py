'''PSCP Program'''
def main(data_list, state, powered_on, count):
    '''8356-SceneSwitch I 22/10/2022'''
    while True:
        time = input()
        if time == 'End':
            break
        data_list.append(float(time))
    for i, j in enumerate(data_list):
        powered_on = False if powered_on else True if not powered_on else powered_on
        if j - data_list[i-1] <= 6 and powered_on and i > 0:
            state = 'Warmwhite' if state == 'DayL' else 'DayL' if state == 'Warmwhite' else ''
            count += 1 if state == 'Warmwhite' else 0
        state = 'DayL' if j - data_list[i-1] > 6 and powered_on else state
    print(count)
main([], 'DayL', False, 0)
