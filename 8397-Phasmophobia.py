'''PSCP Program'''
def main():
    '''8397-Phasmophobia 28/10/2022'''
    ghosts = {"EMF Level 5" : ['Banshee', 'Jinn', 'Oni', 'Phantom', 'Revenant', 'Shade'],
              "Ghost Writing" : ['Demon', 'Oni', 'Revenant', 'Shade', 'Spirit', 'Yurei'],
              "Fingerprints" : ['Banshee', 'Poltergeist', 'Revenant', 'Spirit', 'Wraith'],
              "Spirit Box" : ['Demon', 'Jinn', 'Mare', 'Oni', 'Poltergeist', 'Spirit', 'Wraith'],
              "Freezing Temperatures" : ['Banshee', 'Demon', 'Mare', 'Phantom', 'Wraith', 'Yurei'],
              "Ghost Orb" : ['Jinn', 'Mare', 'Phantom', 'Poltergeist', 'Shade', 'Yurei'],
              "No evidence" : ['Banshee', 'Jinn', 'Oni', 'Phantom', 'Revenant', 'Shade', 'Demon',
                               'Mare', 'Poltergeist', 'Spirit', 'Wraith', 'Yurei']}
    out = list(set(ghosts[input()]).intersection(ghosts[input()]).intersection(ghosts[input()]))
    if out:
        print(*sorted(out), sep='\n')
    else:
        print('Not yet discovered')
main()
