import sys,os

class PollObject:
    def __init__(self, abbr, points):
        self.points = points
        self.abbr = abbr
        # UD = 0, Trump = 1, Biden = 2
        self.cand = 0
        self.obj = {}

states = {}

def getAllStates():
    all_states = open('states.csv', 'r').readlines()
    for state in all_states:
        state_info = state.split(',')
        states[state_info[1]] = PollObject( state_info[0], int(state_info[2].strip()) )

def getData():
    dataset = open("data.csv", "r").readlines()
    for data in dataset:
        curData = data.strip().split('\t')
        curState = curData[0]
        if curData[3] == 'Biden':
            states[curState].cand = 2
        else:
            states[curState].cand = 1

def findReplaceID(curSvg, curAbbr, cand):
    if cand == 1:
        curSvg = curSvg.replace("id=\"" + curAbbr + "\" fill=\"#d3d3d3\"", "id=\"" + curAbbr + "\" fill=\"#ffcccb\"")
    elif cand == 2:
        curSvg = curSvg.replace("id=\"" + curAbbr + "\" fill=\"#d3d3d3\"", "id=\"" + curAbbr + "\" fill=\"#d1edf2\"")
    return curSvg

def editSvg():
    curSvg = open("map.svg", "r").read()
    for key in states:
        #print(states[key].cand)
        curSvg = findReplaceID(curSvg, states[key].abbr, states[key].cand)
    open("newmap.svg", "w").write(curSvg)

    
getAllStates()
getData()
editSvg()