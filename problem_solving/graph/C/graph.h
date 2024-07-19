
#include "queue.h"
#include <stdio.h>
#include <stdlib.h>

#define MAXV 100
#define FALSE 0
#define TRUE 1

typedef struct edgenode {
  int val;
  int weight;
  struct edgenode *next;
} edgenode, *edgenode_ptr;

typedef struct graph {
  edgenode *edges[MAXV + 1]; /* adjacency info */
  int degree[MAXV + 1];      /* out dgree of each vertex */
  int nvertices;
  int nedges;   /* number of edges in the graph */
  int directed; /* is directed */
} graph, *graph_ptr;



edgenode_ptr edgenode_init();
void graph_init(graph_ptr g, int directed);
void insert_edge(graph_ptr g, int x, int y, int directed);
void read_graph(graph_ptr g, int directed);
void print_graph(graph_ptr g);
void init_graph_search(graph_ptr g);
void bfs(graph_ptr g, int start);
void create_small_graph(graph_ptr g);
void processed_vertex_early(int vrtx);
void process_edge(int vrtx, int val);
void process_vertex_late(int v);
void find_path(int start, int end, int parents[]);
