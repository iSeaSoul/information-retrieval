import math

class InvertedNodeWithSkip(object):
    def __init__(self, num):
        self.num = num
        self.skip_node = None
        self.next_node = None

    def set_skip(self, skip_node):
        self.skip_node = skip_node

    def set_next(self, next_node):
        self.next_node = next_node


class SkipLinkedList(object):
    def __init__(self, data = None):
        self.head = None
        self.list_len = 0
        if data:
            self.build(data)

    def build(self, data):
        for item in sorted(data):
            self.append(InvertedNodeWithSkip(item))

    def append(self, appended_node):
        cur = self.head
        if not cur:
            self.head = appended_node
            return
        while cur.next_node:
            cur = cur.next_node
        cur.set_next(appended_node)
        self.list_len += 1

    def skip(self, cur, skip_len):
        while skip_len > 0 and cur:
            cur = cur.next_node
            skip_len -= 1
        return cur

    def build_skip_edge(self):
        self.skip_len = math.sqrt(self.list_len)
        cur = self.head
        next = self.skip(cur, self.skip_len)
        while next:
            cur.set_skip(next)
            cur = next
            next = self.skip(cur, self.skip_len)

    def print_list(self):
        cur = self.head
        while cur.next_node:
            print cur.num,
            if cur.skip_node:
                print '(skip %d)' % (cur.skip_node.num),
            cur = cur.next_node
        print cur.num


def intersection(lista, listb):
    listinter = []
    pa, pb = lista.head, listb.head
    while pa and pb:
        if pa.num == pb.num:
            listinter.append(pa.num)
            pa = pa.next_node
            pb = pb.next_node
        elif pa.num < pb.num:
            if pa.skip_node and pa.skip_node.num <= pb.num:
                pa = pa.skip_node
            else:
                pa = pa.next_node
        else:
            if pb.skip_node and pb.skip_node.num <= pa.num:
                pb = pb.skip_node
            else:
                pb = pb.next_node
    return listinter

def main():
    a = SkipLinkedList([2, 3, 4, 5, 8, 9, 10, 12, 22, 23, 33, 45])
    b = SkipLinkedList([3, 5, 8, 10, 14, 23, 34, 42, 45, 49])
    a.build_skip_edge()
    a.print_list()
    b.build_skip_edge()
    b.print_list()

    print intersection(a, b)

if __name__ == '__main__':
    main()
