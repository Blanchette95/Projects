import random as rand

keys = ['Ab','A','Bb','B','C','Db','D','Eb','E','F','F#/Gb','G']
scales = ['Major', 'Natural Minor', 'Harmonic Minor', 'Melodic Minor']

def print_goodbye():
    print "Good Job!"

def key():
    i = rand.randint(0,11)
    print keys[i]

def scale(scale_list):
    j = rand.randint(0,len(scale_list)-1)
    print scale_list[j]

def main():
    another = 'y'
    scale_list = []
    scale_type = raw_input("Which types of scales do you want to practice? ")
    scale_list += scale_type.strip().split(',')
    while another == 'y':
        key()
        scale(scale_list)
        print #blank
        another = raw_input('Another one? ')
        print #blank
    print_goodbye()
    
if __name__ == "__main__":
    main()
