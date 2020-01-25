import numpy as np
from flaskr.Sentence_Store import SentenceTree
from flaskr import Sentence_Store

arr = None
total_sent_sus = 0
def lev_handler(a,b):
    global arr
    arr = np.zeros((len(a)+1,len(b)+1))

    i=1
    j=1

    while(i<len(a)+1 ):
        j = 1
        while(j<len(b)+1):
            arr[i][j] = lev(a,b,i,j)
            j+=1

        i+=1

    return arr[len(a)][len(b)];


def lev(a,b,i,j):
    if(arr[i][j]!=0):
        return arr[i][j]
    x = None
    y = None
    z = None

    if(min(i,j)==0):
        return max(i,j)
    else:
        x = lev(a,b,i-1,j)+1
        y = lev(a,b,i,j-1)+1
        z = lev(a,b,i-1,j-1)

        if(a[i-1] != b[j-1]):
            z = z + 1
        return min(x,y,z)









def get_then_insert_sentences(suspected_file, st: SentenceTree):

    for x in suspected_file:

        while True:
            if(x=="\n" or x == ""):
                break

            dot_index = x.index(".")
            sentence = x[0:dot_index+1]
            global total_sent_sus
            total_sent_sus +=1
            st.insert(sentence)
            x = x[dot_index+1:] # remaining text


def get_nearest_sentence_and_score(st: SentenceTree,sentence):
    temp = st.root
    ascii1 = 0
    ascii2 = Sentence_Store.str_to_int(sentence)
    edits = 0;
    min_edits = 1000000000
    min_edits_str = ""


    if(temp.sentence == sentence):
        return (sentence,0)
    else:
        while temp!=None:
            if (temp.sentence == sentence):
                return (sentence,0)

            ascii1 = Sentence_Store.str_to_int(temp.sentence)
            edits = lev_handler(temp.sentence,sentence)
            if (edits < min_edits):
                min_edits = edits;
                min_edit_str = temp.sentence;

            if((ascii1 == ascii2) and (sentence!= temp.sentence)):
                temp = temp.right
                continue


            if(ascii1 < ascii2):
                temp = temp.right
                continue
            if(ascii1 > ascii2):
                temp = temp.left
                continue

    return (min_edits_str,min_edits)

def get_plg_score(original_file,suspected_file):
    threshold = 25
    edit_percent = 0
    plg_score = 0
    plg_count = 0
    plg_count = 0
    lev_temp = 0
    st = SentenceTree()
    global total_sent_sus
    total_sent_sus = 0
    get_then_insert_sentences(suspected_file,st)
    sentence = ""
    dot_ind = 0

    for x in original_file:
        while True:
            if(x=="\n" or x == ""):
                break

            dot_index = x.index(".")
            sentence = x[0:dot_index+1]
            nearest_info = get_nearest_sentence_and_score(st,sentence)

            lev_temp = nearest_info[1]
            edit_percent = (lev_temp/len(sentence))*100

            if(edit_percent < threshold):
                plg_count+=1

            x = x[dot_index+1:] # remaining text


    plg_score = (plg_count / total_sent_sus)*100
    print(plg_count)
    print(total_sent_sus)

    return plg_score
