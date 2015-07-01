from chardet.universaldetector import UniversalDetector
from unipath import Path

def read(filename,linesForUniversalDetector=1000):
    lines = [f for f in open(filename,"rb")][0:linesForUniversalDetector]
    detector = UniversalDetector()
    [detector.feed(l) for l in lines]
    detector.close()

    if detector.result['confidence'] < 0.80 :
        return False

    encoding = detector.result['encoding']
    return [l.strip().lower() for l in open(filename,encoding=encoding)]

def read_k90(filename):
    lines=read(filename)
    key_values={}
    for line in lines:
        line=line.split("\t")
        if len(line) < 2 :
            continue
        key=line[0]
        value=int(line[1])
        key_values[key]=value
    return key_values