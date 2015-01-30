def intersect(lista, listb):
    listinter = []
    lena, lenb = len(lista), len(listb)
    idxa, idxb = 0, 0
    while idxa < lena and idxb < lenb:
        if lista[idxa] == listb[idxb]:
            listinter.append(lista[idxa])
            idxa += 1
            idxb += 1
        elif lista[idxa] < listb[idxb]:
            idxa += 1
        else:
            idxb += 1
    return listinter

def intersect_posa_nagb(lista, listb):
    listinter = []
    lena, lenb = len(lista), len(listb)
    idxa, idxb = 0, 0
    while idxa < lena:
        while idxb < lenb and lista[idxa] > listb[idxb]:
            idxb += 1
        if idxb >= lenb or lista[idxa] < listb[idxb]:
            listinter.append(lista[idxa])
        idxa += 1
    return listinter

def union(lista, listb):
    listunion = []
    lena, lenb = len(lista), len(listb)
    idxa, idxb = 0, 0
    while idxa < lena and idxb < lenb:
        if lista[idxa] == listb[idxb]:
            listunion.append(lista[idxa])
            idxa += 1
            idxb += 1
        elif lista[idxa] < listb[idxb]:
            listunion.append(lista[idxa])
            idxa += 1
        else:
            listunion.append(listb[idxb])
            idxb += 1
    while idxa < lena:
        listunion.append(lista[idxa])
        idxa += 1
    while idxb < lenb:
        listunion.append(listb[idxb])
        idxb += 1

    return listunion

def union_posa_nagb(lista, listb, total):
    if not isinstance(total, int):
        raise Exception('Func union_posa_nagb need total(int) arg!')

    listall = [i for i in xrange(1, total + 1)]
    return union(lista, intersect_posa_nagb(listall, listb))

def main():
    a = [1, 2, 4]
    b = [2, 3, 4, 5]
    print intersect(a, b)
    print intersect_posa_nagb(a, b)
    print union(a, b)
    print union_posa_nagb(a, b, 8)

if __name__ == '__main__': main()
