import sys 
sys.path.append("..")
from ezr import adds, SYM, div, csv, COLS, show, SYM, NUM
import random, string, os

def task4():
  #str = ''.join(random.choices(string.ascii_lowercase +
  #                             string.digits, k=10))
  str = '''
    -a --any     #todo's to explore             = 100
    -c --cohen   size of the Cohen d            = 0.35
    -d --decs    #decimals for showing floats   = 3
    -e --enough  want cuts at least this good   = 0.1
    -F --Far     how far to seek faraway        = 0.8
    -h --help    show help                      = False
    -H --Half    #rows for searching for poles  = 128
    -k --k       bayes low frequency hack #1    = 1
    -l --label   initial number for labelling    = 4
    -L --Last    max allow #labelling            = 30
    -m --m       bayes low frequency hack #2    = 2
    -n --n       tinyN                          = 12
    -N --N       smallN                         = 0.5
    -p --p       distance function coefficient  = 2
    -R --Run     start up action method         = help
    -s --seed    random number seed             = 1234567891
    -t --train   training data                  = data/misc/auto93.csv
    -T --test    test data (defaults to train)  = None
    -v --version show version                   = False
    -x --xys     max #bins in discretization    = 16

  '''
  sym = adds(SYM(),[c for c in str])
  print(str, div(sym), sep=" ")

def task5():
    #print(' ' * 30+'x cols'+' ' * 8+'y cols')
    #print(' ' * 30+'-' *11 +' ' *2 +'-' *15)
    open('test.txt', 'w').close()
    header = 'file|'+'x cols|'+'y cols'
    with open("test.txt", "a") as myfile:
      myfile.write(header+"\n")
    csv_files = extract_files("../data")
    for csv_file in csv_files:
        rows = csv(csv_file)
        cols = COLS(next(rows))
        numrows = len(list(rows))
        numcols = len(cols.all)
        print(numcols)
        print(len(cols.x))
        print(len(cols.y))
        xnumssym = sum([1 for col in cols.x if col.this==SYM])
        ynumssym = sum([1 for col in cols.y if col.this==SYM])
        xnumsnum = sum([1 for col in cols.x if col.this==NUM])
        ynumsnum = sum([1 for col in cols.y if col.this==NUM])
        content = csv_file+" "+str(numrows)+" "+str(numcols)
        content+="|"+str(xnumssym)+","+str(xnumsnum)+ "|" + str(ynumssym)+","+str(ynumsnum)
        with open("test.txt", "a") as myfile:
          myfile.write(content+"\n")
def extract_files(directory):
    return (os.path.join(root, file)
            for root, dirs, files in os.walk(directory)
            for file in files
            if file.endswith('.csv'))

def main():
  task5()

if __name__=="__main__":
  main()