def freqQuery(queries):
    '''
https://www.hackerrank.com/challenges/frequency-queries/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps
    Queries: 2-D array of size q quieries[i][0] contains the operation and queries[i][1] contains data element.
    '''
    from collections import Counter
    freq = Counter()

    cnt = Counter()

    arr = []

    for q in queries: #for each tuple
        if q[0]==1:  #if first value equals 1
            cnt[freq[q[1]]]-=1
            freq[q[1]]+=1
            cnt[freq[q[1]]]+=1
            print(cnt)

        elif q[0]==2: #if first value equals 2
            if freq[q[1]]>0: #if the value of second tuple is greater than 0
                cnt[freq[q[1]]]-=1
                freq[q[1]]-=1
                cnt[freq[q[1]]]+=1

        else:
            if cnt[q[1]]>0:
                arr.append(1)
            else:
                arr.append(0)

    return arr

queries = [(1,1), (2,2), (3,2), (1,1), (1,1), (2,1), (3,2)]
print(freqQuery(queries))