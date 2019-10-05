import java.util.*;
import java.io.*;

public class guessthedatastructure {
    // throws a checked IOException for BufferedReader
    public static void main(String args[]) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        // initialize the current line
        String currentLine;
        // while not EOF
        while ((currentLine = reader.readLine()) != null) {
            // convert the first number (representing the number of following line in the current command) as an integer
            int numberLines = Integer.parseInt(currentLine);

            // initialize priority queue as pq, queue as qu, and stack as st
            // Collections.reverseOrder() is added to the priority queue since we want the maximum element first
            PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
            Queue<Integer> qu = new LinkedList<>();
            Stack<Integer> st = new Stack<>();

            // initialize boolean for each data structure to check if they are correct after the operations
            boolean priorityqueue = true;
            boolean queue = true;
            boolean stack = true;

            // for the next lines in the current command
            for (int i = 0; i < numberLines; i++) {
                // reads the next line and split the line into an operation [0] and an element [0]
                String str = reader.readLine();
                String array[] = str.split(" ");
                int operation = Integer.parseInt(array[0]);
                // if the operation is add element (1)
                if (operation == 1) {
                    if (stack) {
                        // push the element [0] onto the stack
                        st.push(Integer.parseInt(array[1]));
                    }
                    if (queue) {
                        // add the element [0] in the queue
                        qu.add(Integer.parseInt(array[1]));
                    }
                    if (priorityqueue) {
                        // add the element [0] in the priority queue
                        pq.offer(Integer.parseInt(array[1]));
                    }
                }
                // if the operation is removing an element (2)
                else if (operation == 2) {

                    // if the stack is empty when trying to pop()
                    // or if the popped element (the most recently added) is not equal to the element returned from the operations,
                    // the data structure is not a stack
                    if (st.size() == 0 || !st.pop().equals(Integer.parseInt(array[1]))) {
                        stack=false;
                    }

                    // if the queue is empty when trying to poll()
                    // or if the polled element (the least recently added) is not equal to the element returned from the operations,
                    // the data structure is not a queue
                    if (qu.size() == 0 || !qu.poll().equals(Integer.parseInt(array[1]))) {
                        queue=false;
                    }

                    // if the priority queue is empty when trying to poll()
                    // or if the polled element (the maximum element) is not equal to the element returned from the operations,
                    // the data structure is not a priority queue
                    if (pq.size() == 0 || !pq.poll().equals(Integer.parseInt(array[1]))) {
                        priorityqueue=false;
                    }
                }

            }

            // if no data structure corresponds to the unknown data structure
            if (!stack && !queue && !priorityqueue) {
                System.out.println("impossible");
            }

            // if more than one data structure correspond
            else if ((stack && queue) || (stack && priorityqueue) || (queue && priorityqueue)) {
                System.out.println("not sure");
            }

            // only the stack
            else if (stack) {
                System.out.println("stack");
            }

            // only the queue
            else if (queue) {
                System.out.println("queue");
            }

            // only the priority queue
            else if (priorityqueue) {
                System.out.println("priority queue");
            }
        }
    }
}
