class SentenceTree:
    def __init__(self):
        self.root: SNode = None



    def insert(self,sentence):
        n = SNode(sentence)
        if(self.root == None):
            self.root = n;
        else:
            temp1 = self.root
            temp2 = self.root

            while temp1 != None:
                temp2 = temp1;
                if(str_to_int(temp1.sentence) <= str_to_int(sentence)):
                    temp1 = temp1.right

                else:
                    temp1 = temp1.left

            if(str_to_int(temp2.sentence) <= str_to_int(sentence)):
                temp2.right = n

            else:
                temp2.left = n



    def lnr(self,n):

        if(n!=None):

            self.lnr(n.left)
            print(n.sentence)
            self.lnr(n.right)






def str_to_int(str):
    ascii_sum = 0
    for s in str:
        ascii_sum += ord(s)

    return ascii_sum


        



class SNode:
    def __init__(self,sentence):
        self.sentence = sentence
        self.left = None
        self.right = None




