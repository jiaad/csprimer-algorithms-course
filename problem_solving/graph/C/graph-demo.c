#include "graph.h"

extern int parent[];


void processed_vertex_early(int vrtx) {}
void process_edge(int vrtx, int val) {
  printf("processed edge (%d,%d)\n", vrtx, val);
}
void process_vertex_late(int v) {}
int main(void) {
  graph G;
  // G = malloc(sizeof(graph));
  // graph_init(&G, 0);
  // rintf("nv: %d - ne: %d - nd: %d\n", G.nvertices, G.nedges, G.directed);
  //  read_graph(&G, 1);
  printf("the size of G: %ld\n", sizeof(G));
  create_small_graph(&G);
  print_graph(&G);
  printf("\n-----------------\n");
  bfs(&G, 1);
  printf("\n");
  find_path(1, 20, parent);

  return 0;
}

/**
 * THE TRAVERSAL OF A ADJACENCY LIST
 * N = number of vertices
 * M = number of edges(connection)
 *
 * Ø(N + M) // M is the total number of connection
 *
 *
 */
