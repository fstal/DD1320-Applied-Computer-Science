from classes import Song
import timeit


def song_reader():
    """
    Reads file, splits rows by the separator to a list and sends row
    by row to object_creator()
    :return:
    """
    with open('unique_tracks.txt', 'r') as read:
        # with open('unique_tracks.txt', 'r') as read:
        for row in read:
            row_list = row.strip().split('<SEP>')
            object_creator(row_list)


def object_creator(row_list):
    """
    Takes row_lists and creates a Song-object.
    Adds these to a separate dictionary and a list
    :param row_list:
    :return:
    """
    song_object = Song(row_list[0], row_list[1], row_list[2], row_list[3])
    #song_list.append(song_object)
    if row_list[2] in song_dict:
        song_dict[row_list[2]].append(song_object)
    else:
        song_dict[row_list[2]] = [song_object]


def sequential_search(song_list, song_search):
    """
    Unsure how python so efficiently uses the for loop compared to the manual
    iteration with pos +=1, seems to work like a charm.
    Searches by working its way thru elements of the list one-by-one
    """
    found = False
    for obj in song_list:
        if song_search == obj.song_name:
            # print("seq search #1: Found it!")
            found = True
            break
    return found


def sequentialsearch(song_list, song_search):
    """
    Borrowed from https://interactivepython.org/runestone/static/pythonds/SortSearch/Thesequentialsearch.html
    with modifications.
    The books way of doing an sequential search
    :param song_list:
    :return:
    """
    pos = 0
    found = False
    while pos < len(song_list) and not found:
        if song_list[pos].song_name == song_search:
            # print("seq search #2 : Found it!")
            found = True
        else:
            pos += 1
    return found


def binarysearch(song_list, song_search):
    """
    Borrowed from https://interactivepython.org/runestone/static/pythonds/SortSearch/TheBinarySearch.html
    with some modifications
    :param song_list:
    :param song_search:
    :return:
    """
    testing_list_binary.append(len(song_list))
    if len(song_list) == 0:
        # print("BS: List is too short, did you sort the list properly? Does the song exist?")
        return False
    else:
        midpoint = len(song_list)//2
        if song_list[midpoint].song_name == song_search:
            # print("BS : Well i'll be damned, found the lil' fella'")
            return True
        else:
            if song_search < song_list[midpoint].song_name:
                binarysearch(song_list[:midpoint], song_search)
            else:
                binarysearch(song_list[midpoint+1:], song_search)


def merge_sort(song_list):
    """
    Borrowed from https://interactivepython.org/runestone/static/pythonds/SortSearch/TheMergeSort.html
    :param song_list:
    :return:
    """
    if len(song_list) > 1:
        mid = len(song_list)//2
        lefthalf = song_list[:mid]
        righthalf = song_list[mid:]

        merge_sort(lefthalf)
        merge_sort(righthalf)

        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                song_list[k] = lefthalf[i]
                i += 1
            else:
                song_list[k] = righthalf[j]
                j += 1
            k += 1

        while i < len(lefthalf):
            song_list[k] = lefthalf[i]
            i += 1
            k += 1

        while j < len(righthalf):
            song_list[k] = righthalf[j]
            j += 1
            k += 1


def dict_search(song_dict, search_key):
    """
    Checks for key in dict, if found returns the values for that key
    :param song_dict:
    :return:
    """
    if search_key in song_dict:
        # for obj in song_dict[dict_key]:
        #    print(obj.song_name)
        return True
    else:
        # print("No such key exists in dictionary")
        return False

def analysis_linear(time_list, testing_list):
    i = 1
    for name in testing_list:
        lineartimer = timeit.timeit(stmt=lambda: sequentialsearch(song_list, name), number=50)
        time_list.append(round(lineartimer, 4))
    print(time_list)
    for time in time_list:
        time_list[i-1] = round(((i*50000)/time)/100000)
        i += 1
    print(time_list)


def analysis_dict_search(time_list, testing_list):
    i = 1
    for artist in testing_list:
        dicttimer = timeit.timeit(stmt=lambda: dict_search(song_list, artist), number=10)
        time_list.append(dicttimer)
    print(time_list)
    for time in time_list:
        time_list[i-1] = round(time, 4)
        i += 1
    print(time_list)

def timer_all():
    """
    Measures time for all dem functions
    :return:
    """
    mergesorttime = timeit.timeit(stmt=lambda: merge_sort(song_list), number=1)
    print("The mergesort took ", round(mergesorttime, 4), "seconds")

    binarytime = timeit.timeit(stmt=lambda: binarysearch(song_list, song_search), number=1)
    print("The binary search took ", round(binarytime, 4), "seconds")

    lineartime1 = timeit.timeit(stmt=lambda: sequential_search(song_list, song_search), number=1)
    print("The sequential #1 search took ", round(lineartime1, 4), "seconds")

    lineartime2 = timeit.timeit(stmt=lambda: sequentialsearch(song_list, song_search), number=1)
    print("The sequential #2 search took ", round(lineartime2, 4), "seconds")

    dictsearchtime = timeit.timeit(stmt=lambda: dict_search(song_list, "ifnaisfniasnf"), number=1)
    print("The dict search took ", round(dictsearchtime, 4), "seconds")


song_search = "Fiiiiinns inteee"                         # Sista låt i osort, Ferneh....
song_list = []
song_dict = {}
song_reader()                                           # Läser in alla låtar i dict + list
time_list = []
testing_list_binary = []
#timer_all()

dictsearchtime = timeit.timeit(stmt=lambda: dict_search(song_dict, "sajsdkofnisadnif"), number=50000)
print("The dict took ", round(dictsearchtime, 4), "seconds")

#timer_all()
#merge_sort(song_list)
#for i in range(3):
#    print(i)
#    timer_all()

#merge_sort(song_list)
#print(len(testing_list_binary))


# print(len(song_list))                           # Kollar längderna
# print(len(song_dict))

# timer_all()
# merge_sort(song_list)
# print(len(song_list))
# binarysearch(song_list, song_search)


# merge_sort(song_list)                         # Kör merge_sort(), måste ske innan bs
# last_artist = song_list[len(song_list)-1]     # Testar att vi har korrekt inläsning, med sista låt och artist
# print(last_artist.artist)
# print(last_artist.song_name)

# dict_search(song_dict)                         # Kör dict_search() och letar efter dict_key

#timer_all()

# binarysearch(song_list, song_search)          # Binsearch, letar efter song_search, endast i sorterad

# sequential_search(song_list, song_search)     # Linjärsökning
# sequentialsearch(song_list, song_search)


#Code for analysing dict_search
"""
testing_list_dict = []
for k in range(20):
    testing_list_dict.append(song_list[3000 * (k+1)].song_name)
analysis_dict_search(time_list, testing_list_dict)
"""

#Code for analysing sequential search
"""
testing_list_sequential = []
for k in range(20):
    testing_list_sequential.append(song_list[49998*(k+1)].song_name)
analysis_linear(time_list, testing_list_sequential)
"""

"""
-----Analys------

Linjärsökning:
[0, 1, 1, 1, 1, 1, 1, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 36, 2, 1] -> Analysis for linear search
Söktiden ser vi är direkt proportionell mot indexet där vi har valt vårt ord. Vi kan därför dra
slutsatsen att tidskomplexiteten är O(n)
Siffrorna i listan motsvarar position/(tid*10000). Då nästan alla siffror ligger kring 1
kan vi dra slutsatsen att positionen och tiden är proportionerliga

Binärsökning:
print(len(testing_list_binary)) ger längden 20. Denna längd är antalet gånger som listan
slice:as i sökningen vid värsta fallet. Detta ger (1000000)*(1/2)^20 = 1 (ungefär)
(n/2^i = 1 där n är listans längd och i är antalet sökningar --> Detta gället om allt är korrekt)
Därmed stämmer vår komplexitet

Mergesort:
Mergesort har en tidskomplexitet på nlog(n) där n är antalet element. Detta kan testas om vi har värsta
scenariot av vår original lista. Då vi inte har det kan vi inte testa detta optimalt för vår fil.
Då vi dessutom använder list slices i vår kod kommer det inte ge optimalt resultat. Komplexiteten
i vår kod är alltså något högre än vad en optimal mergesort har.
(Visas även under redovisningen på papper)

Dicttionary sökning:
Söker vi i vårt dictionary med olika ord och spara alla tider får vi exempelvis följande
[1.2046, 1.1843, 1.1933, 1.1524, 1.1631, 1.1716, 1.1628, 1.1674, 1.2216, 1.1697, 1.147, 1.1735, 1.1766, 1.1792, 1.1514, 1.1684, 1.1679, 1.1688, 1.1548, 1.1984] (sekunder)
Siffrorna innebär att det bara skiljer väldigt lite mellan varje sökning.
Vi anser alltså att detta är O(1) komplexitet.
"""




"""
def binarysearch2(sorted_song_list, song_search):

    if len(sorted_song_list) == 0:
        print("BS: List is too short, did you sort the list properly? Does the song exist?")
        return False
    else:
        midpoint = len(sorted_song_list)//2
        if sorted_song_list[midpoint].song_name == song_search:
            # print("BS : Well i'll be damned, found the lil' fella'")
            return True
        else:
            if song_search < sorted_song_list[midpoint].song_name:
                binarysearch(sorted_song_list[:midpoint], song_search)
            else:
                binarysearch(sorted_song_list[midpoint+1:], song_search)


def please_tell_me_were_not_allowed_to_do_this(song_list):
    sorted_song_list = sorted(song_list, key=lambda x: x.song_name)
    return sorted_song_list


    # please_no = timeit.timeit(stmt=lambda: please_tell_me_were_not_allowed_to_do_this(song_list), number=1)
    # print("The please dont do this took ", round(please_no, 4), "seconds")




Slutsats om mergesort.
Best case: Allt är redan sorterat. Om vi kör mergesort på en redan sorterad lista bör vi få samma svar på
worst case sequentialsearch
Worst case: nlogn.
Vårt fall ligger clearly mitt emellan (n*[tid för worst case binary])] och O(n)
Vilket är så mycket vi kan testa utan att få aids.

"""
