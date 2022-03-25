from __future__ import annotations
from email import iterators
from typing import Any, Type


class Node:
    def __init__(self, data: Any = None, next: Node = None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self) -> None:
        self.no = 0
        self.head = None
        self.current = None

    def __len__(self) -> int:
        return self.no

    def search(self, data: Any) -> int:
        cnt = 0
        ptr = self.head
        while ptr is not None:
            if ptr.data == data:
                self.current = ptr
                return cnt
            cnt += 1
            ptr = ptr.next
        return -1

    def __contains__(self, data: Any) -> bool:
        return self.search(data) >= 0

    def add_first(self, data: Any) -> None:
        ptr = self.head
        self.head = self.current = Node(data, ptr)
        self.no += 1

    def add_last(self, data: Any) -> None:
        if self.head is None:
            self.add_first(data)
        else:
            ptr = self.head
            while ptr.next is not None:
                ptr = ptr.next
            ptr.next = Node(data, None)
            self.no += 1

    def remove_first(self) -> None:
        if self.head is not None:  # 삭제 처리를 수행하는 것은 리스트가 비어 있지 않을 떄 가능
            self.head = self.current = self.head.next
        self.no -= 1

    def remove_last(self) -> None:
        if self.head is not None:  # 삭제 처리를 수행하는 것은 리스트가 비어 있지 않을 떄 가능
            if self.head.next is None:  # 노드가 하나 뿐이라면
                self.remove_first()
            else:
                ptr = self.head
                pre = self.head
                while ptr.next is not None:  # 꼬리 노드와 맨끝에서 2번쨰 노드를 찾는다.
                    pte = ptr  # 스캔 중인 노드의 앞쪽 노드를 참조하는 변수
                    ptr = ptr.next
                pre.next = None
                self.current = pre
                self.no -= 1

    def remove(self, p: Node) -> None:
        if self.head is not None:
            if p is self.head:  # p가 head node일 경우
                self.remove_first()
            else:
                ptr = self.head

                while ptr.next is not p:
                    ptr = ptr.next
                    if ptr is None:
                        return
                ptr.next = p.next  # node p는 어디에서도 참조되지 않게된다.
                self.current = ptr
                self.no -= 1

    def remove_current_node(self) -> None:
        if self.head is not None:
            if self.current is not None:
                if self.current is self.head:
                    self.remove_first()
                else:
                    ptr = self.head

                    while ptr.next is not self.current:
                        ptr = ptr.next
                        if ptr is None:
                            return
                    ptr.next = self.current.next
                    self.current = ptr
                    self.no -= 1

    def clear(self) -> None:
        self.__init__(self)

    def next(self) -> None:
        if self.head is not None:
            if self.current is not None:
                self.current = self.currnet.next
                return True
        return False

    def print_currnet_noe(self) -> None:
        if self.current is None:
            print("주목 노드가 존재하지 않습니다.")
        else:
            print(self.current.data)

    def print(self) -> None:
        ptr = self.head

        while ptr is not None:
            print(ptr.data)
            ptr = ptr.next
    # __next__()함수를 갖는 이터레이터를 반환하는 __iter__()함수를 구현한다.

    def __iter__(self) -> iterators:
        return LinkedListIterator(self.head)  # 초기화 후 이터레이터 반환
        '''
         in Python, the next method is called automatically to get each item from the iterator, thus going through the process of iteration.  iterator is an object with a next (Python 2) or __next__ (Python 3) method.
        '''


class LinkedListIterator:
    def __init__(self, head: Node):
        self.current = head

    def __iter__(self) -> LinkedListIterator:
        return self

    # __next__() 함수는 다음 원소를 꺼내 반환하는데, 반환하는 원소가 없으면 StopIteration 예외처리를 내보낸다.
    def __next__(self) -> Any:
        if self.current is None:
            raise StopIteration
        else:
            data = self.current.data
            self.current = self.current.next
            return data


if __name__ == '__main__':
    lnklst = LinkedList()

    for i in range(10):
        lnklst.add_last(i)

    lnklstitr = iter(lnklst)
    print(lnklstitr)

    for _ in range(11):
        print(lnklstitr.__next__())
