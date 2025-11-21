package tree;
// 백준 실버2 11725
// 트리의 부모 찾기

/**
 * 큐에서 현재 노드(current)를 꺼냄
 * 그와 연결된 자식(next)을 봤을 때:
 * 아직 parent[next]가 비어 있으면 → current가 부모임
 * 여기서 바로 parent[next] = current 하면 끝남
 */

import java.io.*;
import java.util.*;

public class findParent {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        List<List<Integer>> graph = new ArrayList<>();
        for (int i = 0; i <= n; i++) {
            graph.add(new ArrayList<>());
        }

        for (int i = 0; i < n - 1; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            graph.get(a).add(b);
            graph.get(b).add(a);
        }

        int[] parents = new int[n + 1];
        boolean[] visited = new boolean[n + 1];

        Queue<Integer> q = new LinkedList<>();
        q.offer(1);
        visited[1] = true;

        while (!q.isEmpty()) {
            int current = q.poll();

            for (int next : graph.get(current)) {
                if (!visited[next]) {
                    visited[next] = true;
                    parents[next] = current;
                    q.offer(next);
                }
            }
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 2; i <= n; i++) {
            sb.append(parents[i]).append("\n");
        }
        System.out.println(sb);
    }
}
