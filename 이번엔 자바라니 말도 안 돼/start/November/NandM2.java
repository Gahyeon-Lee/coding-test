package November;

/**
 * 2025년 11월 21일
 * 백트래킹 연습 - 실버3 (15650)
 * N과 M (2)
 */

import java.util.*;

public class NandM2 {
    static int n, m;
    static int[] arr;
    static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        m = sc.nextInt();

        arr = new int[m];

        backtracking(1, 0);
        System.out.println(sb);
    }

    static void backtracking(int start, int depth) {
        if (depth == m) {
            for (int i = 0; i < m; i++) {
                sb.append(arr[i]).append(" ");
            }
            sb.append("\n");
            return;
        }

        for (int i = start; i <= n; i++) {
            arr[depth] = i;
            backtracking(i + 1,  depth+ 1);
        }
    }
}
