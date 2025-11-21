package tree;

// 백준 실버1 1991
//트리순회

import java.io.*;
import java.util.*;

public class TreeTraversal {
    static int[] left = new int[26];
    static int[] right = new int[26];

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            char parent = st.nextToken().charAt(0);
            char l = st.nextToken().charAt(0);
            char r = st.nextToken().charAt(0);

            int p = parent - 'A';

            left[p] = (l == '.') ? -1 : (l - 'A');
            right[p] = (r == '.') ? -1 : (r - 'A');
        }

        preOrder(0);
        System.out.println();
        inOrder(0);
        System.out.println();
        postOrder(0);
        System.out.println();
    }

    static void inOrder(int node) {
        if (node == -1) return;
        inOrder(left[node]);
        System.out.print((char)(node + 'A'));
        inOrder(right[node]);
    }

    static void preOrder(int node) {
        if (node == -1) return;
        System.out.print((char)(node + 'A'));
        preOrder(left[node]);
        preOrder(right[node]);
    }

    static void postOrder(int node) {
        if (node == -1) return;
        postOrder(left[node]);
        postOrder(right[node]);
        System.out.print((char)(node + 'A'));
    }
}
