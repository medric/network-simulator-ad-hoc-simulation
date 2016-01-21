#pattern ->
#$node_(0) set X_ 5.0
#$node_(0) set Y_ 5.0
#$node_(0) set Z_ 0.0
#$node_(1) set X_ 490.0
#$node_(1) set Y_ 285.0
#$node_(1) set Z_ 0.0
#$node_(2) set X_ 150.0
#$node_(2) set Y_ 240.0
#$node_(2) set Z_ 0.0
## Generation of movements
#$ns at 10.0 "$node_(0) setdest 250.0 250.0 3.0"
#$ns at 15.0 "$node_(1) setdest 45.0 285.0 5.0"
#$ns at 110.0 "$node_(0) setdest 480.0 300.0 5.0"
import sys
import argparse
import time
import random
from random import randint

parser = argparse.ArgumentParser(description='AODV')
parser.add_argument('-n', metavar='nodes', type=int)
parser.add_argument('-a', metavar='area', nargs='+', type=float)
parser.add_argument('-v', metavar='velocity', type=float)
parser.add_argument('-d', metavar='duration', type=float)

def main():
    args = parser.parse_args()
    
    nodes = args.n
    area = {'width': args.a[0], 'height': args.a[1]}
    velocity = args.v
    duration = args.d
    
    text = define_pos(area, nodes)
    text += '## Generation of movements\n'
    print 'Generation of movements'
    text += move(area, nodes, velocity, duration)
    
    write(str(text))
    print 'Script successfully executed'
    
def define_pos(area, nodes):
    output = ''
    for n in range(0, nodes):
        output += '$node_(%d) set X_ (%f)\n' % (n, get_random_pos_x(area))
        output += '$node_(%d) set Y_ (%f)\n' % (n, get_random_pos_y(area))
        output += '$node_(%d) set Z_ (%f)\n' % (n, 0.0)
    
    return output
    
def move(area, nodes, velocity, duration):
    output = ''
    timeout = time.time() + duration
    while time.time() < timeout:
        output += 'ns at %f $node_(%d) setdest %f %f %f\n' % (random.uniform(0, duration), randint(0, nodes), get_random_pos_x(area), get_random_pos_y(area), velocity)
    
    return output
        
def get_random_pos_x(area):
    return random.uniform(0, area.get('width'))

def get_random_pos_y(area):
    return random.uniform(0, area.get('height'))

def write(text):
    f = open('setdest.txt','w')  
    f.seek(0)
    f.write(text) # python will convert \n to os.linesep
    f.close()

if __name__ == '__main__':
    main()