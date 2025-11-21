package array;

import java.io.*;
import java.util.*;

public class rotateArray {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        StringBuilder sb = new StringBuilder();
        int t = sc.nextInt();

        while (t != 0) {
            int n = sc.nextInt();
            int degree = sc.nextInt();

            int[][] graph = new int[n][n];

            for (int i = 0; i < n; i++) {
                graph[0][i] = sc.nextInt();
            }

            int k = ((degree / 45) % 8 + 8) % 8;  // 음수 처리
            int mid = n / 2;

            // 라인 8개를 미리 저장해둔다
            List<int[]> lines = new ArrayList<>();

            // 1. 위 중앙 (0, mid)
            lines.add(new int[n]);
            for (int i = 0; i < n; i++) {
                lines.get(0)[i] = graph[i][mid];
            }

            // 2. 오른위 대각선 (i, i)
            lines.add(new int[n]);
            for (int i = 0; i < n; i++) {
                lines.get(1)[i] = graph[i][i];
            }

            // 3. 오른쪽 중앙 (mid, i)
            lines.add(new int[n]);
            for (int i = 0; i < n; i++) {
                lines.get(2)[i] = graph[mid][i];
            }

            // 4. 오른아래 대각선 (n-1-i, i)
            lines.add(new int[n]);
            for (int i = 0; i < n; i++) {
                lines.get(3)[i] = graph[n - 1 - i][i];
            }

            // 5. 아래 중앙 (i, mid)
            lines.add(new int[n]);
            for (int i = 0; i < n; i++) {
                lines.get(4)[i] = graph[i][mid];
            }

            // 6. 왼아래 대각선 (i, n-1-i)
            lines.add(new int[n]);
            for (int i = 0; i < n; i++) {
                lines.get(5)[i] = graph[i][n - 1 - i];
            }

            // 7. 왼쪽 중앙 (mid, i)
            lines.add(new int[n]);
            for (int i = 0; i < n; i++) {
                lines.get(6)[i] = graph[mid][i];
            }

            // 8. 왼위 대각선 (i, mid)
            lines.add(new int[n]);
            for (int i = 0; i < n; i++) {
                lines.get(7)[i] = graph[i][mid];
            }

            // 회전: 8개의 라인을 shift
            int[][] newLines = new int[8][n];
            for (int i = 0; i < 8; i++) {
                newLines[(i + k) % 8] = lines.get(i);
            }

            // 회전된 값을 다시 graph에 넣기
            // 1. 위 중앙
            for (int i = 0; i < n; i++) {
                graph[i][mid] = newLines[0][i];
            }

            // 2. 오른위 대각선
            for (int i = 0; i < n; i++) {
                graph[i][i] = newLines[1][i];
            }

            // 3. 오른쪽 중앙
            for (int i = 0; i < n; i++) {
                graph[mid][i] = newLines[2][i];
            }

            // 4. 오른아래 대각선
            for (int i = 0; i < n; i++) {
                graph[n - 1 - i][i] = newLines[3][i];
            }

            // 5. 아래 중앙
            for (int i = 0; i < n; i++) {
                graph[i][mid] = newLines[4][i];
            }

            // 6. 왼아래 대각선
            for (int i = 0; i < n; i++) {
                graph[i][n - 1 - i] = newLines[5][i];
            }

            // 7. 왼쪽 중앙
            for (int i = 0; i < n; i++) {
                graph[mid][i] = newLines[6][i];
            }

            // 8. 왼위 대각선
            for (int i = 0; i < n; i++) {
                graph[i][mid] = newLines[7][i];
            }

            // 출력
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    sb.append(graph[i][j]).append(" ");
                }
                sb.append("\n");
            }
        }

        System.out.print(sb.toString());
    }

}
