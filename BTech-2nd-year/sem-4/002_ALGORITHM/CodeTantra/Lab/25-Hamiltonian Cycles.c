#include<stdio.h>

#include<stdlib.h>

#include <stdbool.h>

int V;
void printSolution(int path[]);
bool isSafe(int v, bool ** graph, int path[], int pos) {
  if (graph[path[pos - 1]][v] == 0)
    return false;
  for (int i = 0; i < pos; i++)
    if (path[i] == v)
      return false;
  return true;
}
bool hamCycleUtil(bool ** graph, int path[], int pos) {
  if (pos == V) {
    if (graph[path[pos - 1]][path[0]] == 1)
      return true;
    else
      return false;
  }
  for (int v = 1; v < V; v++) {
    if (isSafe(v, graph, path, pos)) {
      path[pos] = v;
      if (hamCycleUtil(graph, path, pos + 1) == true)
        return true;
      path[pos] = -1;
    }
  }
  return false;
}
bool hamCycle(bool ** graph) {
  int * path = (int * ) malloc(V * sizeof(int));
  for (int i = 0; i < V; i++)
    path[i] = -1;
  path[0] = 0;
  if (hamCycleUtil(graph, path, 1) == false) {
    printf("Solution does not exist");
    free(path);
    return false;
  } else {
    printSolution(path);
    free(path);
    return true;
  }
}
void printSolution(int path[]) {
    printf("Following is one Hamiltonian Cycle: \n");
    for (int i = 0; i < V; i++)
        printf("%d",path[i]);
    printf("0");

}
int main() {
  printf("Number of vertices: ");
  scanf("%d", & V);
  bool ** graph = (bool ** ) malloc(V * sizeof(bool * ));
  for (int i = 0; i < V; i++)
    graph[i] = (bool * ) malloc(V * sizeof(bool));
  printf("Enter the adjacency matrix:\n");
  for (int i = 0; i < V; i++)
    for (int j = 0; j < V; j++)
      scanf("%d", & graph[i][j]);
  hamCycle(graph);
  for (int i = 0; i < V; i++)
    free(graph[i]);
  free(graph);
  return 0;
}