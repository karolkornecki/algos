import edu.princeton.cs.algs4.StdRandom;

import java.util.Iterator;
import java.util.NoSuchElementException;

public class RandomizedQueue<Item> implements Iterable<Item> {

    private static final int INITIAL = 10;
    private Item[] items;
    private int size = 0;

    // construct an empty randomized queue
    public RandomizedQueue() {
        this.items = (Item[]) new Object[INITIAL];
    }

    private void resize(int length) {
        Item[] newItems = (Item[]) new Object[length];
        int i = 0;
        int j = 0;
        while (i < items.length) {
            if (items[i] == null) {
                i++;
                continue;
            }
            newItems[j++] = items[i++];
        }
        items = newItems;
    }

    // is the randomized queue empty?
    public boolean isEmpty() {
        return size() == 0;
    }

    // return the number of items on the randomized queue
    public int size() {
        return size;
    }

    // add the item
    public void enqueue(Item item) {
        if (item == null) {
            throw new IllegalArgumentException();
        }
        if (size() == items.length) {
            resize(2 * items.length);
        }
        int i = 0;
        while (items[i] != null) {
            i = (i + 1) % items.length;
        }
        items[i] = item;
        size++;
    }

    // remove and return a random item
    public Item dequeue() {
        if (isEmpty()) {
            throw new NoSuchElementException();
        }
        int random = StdRandom.uniformInt(items.length);
        while (items[random] == null) {
            random = (random + 1) % items.length;
        }
        Item item = items[random];
        items[random] = null;
        size--;
        if (size <= items.length / 4 && items.length / 4 > INITIAL) {
            resize(items.length / 2);
        }
        return item;
    }

    // return a random item (but do not remove it)
    public Item sample() {
        if (isEmpty()) {
            throw new NoSuchElementException();
        }
        int random = StdRandom.uniformInt(size());
        while (items[random] == null) {
            random = (random + 1) % items.length;
        }
        return items[random];
    }

    // return an independent iterator over items in random order
    public Iterator<Item> iterator() {
        Item[] dest = (Item[]) new Object[size];
        int[] indexes = new int[size];
        int j = 0;
        for (int i = 0; i < items.length; i++) {
            if (items[i] != null) {
                indexes[j] = i;
                j++;
            }
        }
        StdRandom.shuffle(indexes);

        for (int i = 0; i < indexes.length; i++) {
            dest[i] = items[indexes[i]];
        }
        return new RandomizedQueueIterator(dest);
    }

    private class RandomizedQueueIterator implements Iterator<Item> {

        private final Item[] items;
        private int pos = 0;

        public RandomizedQueueIterator(Item[] items) {
            this.items = items;
        }

        @Override
        public boolean hasNext() {
            return pos < items.length;
        }

        @Override
        public Item next() {
            if (pos >= items.length) {
                throw new NoSuchElementException();
            }
            return items[pos++];
        }

        @Override
        public void remove() {
            throw new UnsupportedOperationException();
        }
    }

    // unit testing (required)
    public static void main(String[] args) {
    }
}