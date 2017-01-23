file = open('rosalind_subs.txt','r')
f = file.readlines()
DNA = ''
motif = ''
for i in f:
    insert = i.strip('\n')
    if f.index(i)==0:
        DNA = insert
    else:
        motif = insert
#the above code loads the txt file data into strings that I can work with and
#manipulate. In in the 'for' loop I designated that I want the first item on the
#list to be assigned as DNA and the motif is whatever is not the first item in
#the two item list


#I want to scan the string starting at the first character and check if the
#first 4 characters(the length of the motif) equal to the motif.
#2. If it is true that the string equals the motif then I can add the first
#character of the "scan session" to a list
position_of_mot = []
stringindex = []
for i in range(0, len(DNA)):            #I need to do this index list because
                                        #direct string to list gets python confused
                                        #about the true postion of a nucleotide
    stringindex.append(i)
for i in stringindex:
    indexnum = i
    frame = []
    if indexnum == (len(DNA)-len(motif)+1):
        break
    for i in range(indexnum,indexnum+len(motif)):
        frame.append(DNA[i])
        if len(frame) == len(motif):
            framejoined = ''.join(frame)
            if framejoined==motif:
                position_of_mot.append(indexnum+1)      #I add 1 because python
                                                        #starts to count at 0,
                                                        #but we count the first
                                                        #nucleotide as 1
final = []
for i in position_of_mot:
    insert = str(i)+' '
    final.append(insert)
print(''.join(final))
