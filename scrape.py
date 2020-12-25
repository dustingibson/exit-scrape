import requests, sys
import json

class PollObject:
    def __init__(self, points):
        self.points = points
        self.obj = {}

states = {}

def getAllStates():
    all_states = open('states.csv', 'r').readlines()
    for state in all_states:
        state_info = state.split(',')
        states[state_info[1]] = PollObject( int(state_info[2].strip()) )

def getAllScrapes():
    for key in states:
        try:
            url = "https://www.nytimes.com/interactive/2020/11/03/us/elections/ap-polls-" + key + ".html"
            jsonText = requests.get(url)
            open('json/' + key + '.json', 'w').write( jsonText.text  )
        except:
            print("Unexpected error:", sys.exc_info()[0])
            print('Cannot download ' + key)

def jsonTest():
    content = open('json/AL.json', 'r').read()
    cont = json.loads(content)
    print(cont['exitPollSubsetKey'])

def getValue(fname, findTxt, nextTxt, endTxt):
    txt = open(fname, 'r').read()
    markerIdx = txt.find(findTxt)
    if markerIdx < 0:
        return "NA"
    nextIdx = txt[markerIdx:].find(nextTxt)
    if nextIdx < 0:
        return "NA"
    endIdx = txt[markerIdx:][nextIdx:].find(endTxt)
    if endIdx < 0:
        return "NA"
    tol = nextIdx - endIdx
    return txt[markerIdx:][nextIdx:][len(nextTxt):endIdx]

def getAllVals(keyword):
    for key in states:
        fname = 'json/' + key + '.json'
        trump = getValue(fname, '<td class="g-cat"><div> ' + keyword + ' <span class="g-voter-percent">', 'g-cand-trump"> <div>', '</div')
        biden = getValue(fname, '<td class="g-cat"><div> ' + keyword + ' <span class="g-voter-percent">', 'g-cand-biden"> <div>', '</div')
        if trump != "NA" and biden != "NA":
            try:
                if int(trump) > int(biden):
                    print(key + "," + trump + "," + biden + "," + "Trump")
                else:
                    print(key + "," + trump + "," + biden + "," + "Biden")
            except:
                pass
        else:
            #print(key + "," + "ERROR")
            pass
        #if val == None:
        #    print(key)

cmd = sys.argv[1]
keyword = sys.argv[2]

getAllStates()
if cmd == "get":
    getAllScrapes()
elif cmd == "data":
    getAllVals(keyword)