package November;

/**
 * 2025년 11월 21일
 * 백트래킹 연습 - 실버3 (15649)
 * N과 M (1)
 */

import java.util.*;

public class NandM1 {
    static int n, m;
    static boolean[] visited;
    static int[] arr;
    static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        m = sc.nextInt();

        visited = new boolean[n + 1];
        arr = new int[m];

        backtracking(0);
        System.out.print(sb);
    }

    static void backtracking(int depth) {
        if (depth == m) {
            for (int i = 0; i < m; i++) {
                sb.append(arr[i]).append(" ");
            }
            sb.append('\n');
            return;
        }

        for (int i = 1; i <= n; i++) {
            if (!visited[i]) {
                visited[i] = true;
                arr[depth] = i;
                backtracking(depth + 1);
                visited[i] = false;

            }
        }
    }
}
