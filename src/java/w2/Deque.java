import java.util.Iterator;
import java.util.NoSuchElementException;

public class Deque<Item> implements Iterable<Item> {

    private int size = 0;
    private Node head;
    private Node tail;

    // construct an empty deque
    public Deque() {
    }

    // is the deque empty?
    public boolean isEmpty() {
        return size() == 0;
    }

    // return the number of items on the deque
    public int size() {
        return size;
    }

    // add the item to the front
    public void addFirst(Item item) {
        if (item == null) {
            throw new IllegalArgumentException();
        }
        Node node = new Node(item);
        if (head == null && tail == null) {
            head = node;
            tail = node;
        } else {
            assert head != null;
            head.prev = node;
            node.next = head;
            head = node;
        }
        size++;
    }

    // add the item to the back
    public void addLast(Item item) {
        if (item == null) {
            throw new IllegalArgumentException();
        }
        Node node = new Node(item);
        if (head == null && tail == null) {
            head = node;
            tail = node;
        } else {
            node.prev = tail;
            tail.next = node;
            tail = node;
        }
        size++;
    }

    // remove and return the item from the front
    public Item removeFirst() {
        if (isEmpty()) {
            throw new NoSuchElementException();
        }
        Item item = head.value;
        if (head == tail) {
            head = null;
            tail = null;
        } else {
            head = head.next;
            head.prev = null;
        }
        size--;
        return item;
    }

    // remove and return the item from the back
    public Item removeLast() {
        if (isEmpty()) {
            throw new NoSuchElementException();
        }
        Item item = tail.value;
        if (head == tail) {
            head = null;
            tail = null;
        } else {
            tail.prev.next = null;
            tail = tail.prev;
        }
        size--;
        return item;
    }

    // return an iterator over items in order from front to back
    public Iterator<Item> iterator() {
        return new DequeIterator(head);
    }

    private class DequeIterator implements Iterator<Item> {

        private Node node;

        public DequeIterator(Node node) {
            this.node = node;
        }

        @Override
        public boolean hasNext() {
            return node != null;
        }

        @Override
        public Item next() {
            if (node == null) {
                throw new NoSuchElementException();
            }
            Item item = node.value;
            node = node.next;
            return item;
        }

        @Override
        public void remove() {
            throw new UnsupportedOperationException();
        }
    }

    private class Node {
        private final Item value;
        private Node prev;
        private Node next;

        private Node(Item value) {
            this.value = value;
        }
    }

    // unit testing (required)
    public static void main(String[] args) {
        Deque<Integer> deque = new Deque<>();
        System.out.println(deque.isEmpty());
        System.out.println(deque.size);
        deque.addFirst(1);
        System.out.println(deque.isEmpty());
        System.out.println(deque.size);
        System.out.println(deque.removeFirst());
        System.out.println(deque.isEmpty());
        System.out.println(deque.size);
        deque.addLast(2);
        System.out.println(deque.isEmpty());
        System.out.println(deque.size);
        System.out.println(deque.removeLast());
        System.out.println(deque.isEmpty());
        System.out.println(deque.size);
        deque.addFirst(1);
        System.out.println(deque.isEmpty());
        System.out.println(deque.size);
        System.out.println(deque.removeLast());
        System.out.println(deque.isEmpty());
        System.out.println(deque.size);
        deque.addLast(2);
        System.out.println(deque.isEmpty());
        System.out.println(deque.size);
        System.out.println(deque.removeFirst());
        System.out.println(deque.isEmpty());
        System.out.println(deque.size);

        deque.addFirst(1);
        deque.addFirst(11);
        System.out.println(deque.isEmpty());
        System.out.println(deque.size);
        System.out.println(deque.removeFirst());
        System.out.println(deque.isEmpty());
        System.out.println(deque.size);
        System.out.println(deque.removeFirst());
        System.out.println(deque.isEmpty());
        System.out.println(deque.size);

        deque.addLast(1);
        deque.addLast(11);
        System.out.println(deque.isEmpty());
        System.out.println(deque.size);
        System.out.println(deque.removeLast());
        System.out.println(deque.isEmpty());
        System.out.println(deque.size);
        System.out.println(deque.removeLast());
        System.out.println(deque.isEmpty());
        System.out.println(deque.size);
        deque.addLast(1);
        deque.addLast(11);
        System.out.println(deque.isEmpty());
        System.out.println(deque.size);
        System.out.println(deque.removeFirst());
        System.out.println(deque.isEmpty());
        System.out.println(deque.size);
        System.out.println(deque.removeFirst());
        System.out.println(deque.isEmpty());
        System.out.println(deque.size);

        deque.addFirst(3);
        deque.addFirst(2);
        deque.addFirst(1);
        deque.addLast(4);
        deque.addLast(5);
        deque.addLast(6);
        System.out.println(deque.removeFirst());
        System.out.println(deque.removeLast());
        System.out.println(deque.removeFirst());
        System.out.println(deque.removeLast());
        System.out.println(deque.removeFirst());
        System.out.println(deque.removeLast());
        System.out.println(deque.isEmpty());
        System.out.println(deque.size);
        deque.addFirst(3);
        deque.addFirst(2);
        deque.addFirst(1);
        deque.addLast(4);
        deque.addLast(5);
        deque.addLast(6);
        for (Integer integer : deque) {
            System.out.println(integer);
        }
    }
}