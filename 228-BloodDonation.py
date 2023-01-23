'''PSCP Program'''
def main(age, weight, times):
    '''8412-BloodDonation 05/11/2022'''
    consent = (True if input() == 'True' else False) if age == 17 else True
    medical_clr = (True if input() == 'True' else False) if 60 <= age <= 70 else True
    print('Yes' if 17 <= age <= 70 and weight and (True if age <= 55 and times == 0 or \
          times >= 1 else False) and consent and medical_clr else 'No')
main(int(input()), int(input()) >= 45, int(input()))
