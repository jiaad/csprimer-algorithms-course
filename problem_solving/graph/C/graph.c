#include <stdio.h>
#include <stdlib.h>

#define MAXV 100

typedef struct edgenode {
  int y;
  int weight;
  struct edgenode *next;
} edgenode;

typedef struct graph {
  edgenode *edges[MAXV + 1]; /* adjacency info */
  int degree[MAXV + 1];      /* out dgree of each vertex */
  int nvertices;
  int nedges;   /* number of edges in the graph */
  int directed; /* is directed */
} graph, *graph_ptr;

void graph_init(graph_ptr g, int directed) {
  int i; // counter

  g->nvertices = 0;
  g->nedges = 0;
  g->directed = directed;

  for (i = 1; i <= MAXV; i++) {
    g->degree[i] = 0;
  }

  for (i = 1; i <= MAXV; i++) {
    g->edges[i] = NULL;
  }
}

void insert_edge(graph_ptr g, int x, int y, int directed) {
  edgenode *p;
  p = malloc(sizeof(edgenode));

  p->weight = 0;
  p->y = y;
  p->next = g->edges[x];

  g->edges[x] = p;

  g->degree[x]++;

  if (!directed) {
    insert_edge(g, y, x, 1);
  } else {
    g->nedges++;
  }
}

void read_graph(graph_ptr g, int directed) {
  // --
  int i;
  int m;    // number of edges
  int x, y; // vertices in edge (x,y)

  graph_init(g, directed);

  scanf("%d %d", &(g->nvertices), &m);

  for (i = 1; i <= m; i++) {
    scanf("%d %d", &x, &y);
    insert_edge(g, x, y, directed);
  }
}

void print_graph(graph_ptr g) {
  int i;
  int degree;
  edgenode *p;
  for (i = 1; i <= g->nvertices; i++) {
    printf("%d: ", i);
    p = g->edges[i];
    while (p != NULL) {
      printf(" %d", p->y);
      p = p->next;
    }
    printf(" degree: %d", g->degree[i]);
    printf("\n");
  }
}


void create_small_graph(graph_ptr g){
  int m;
  graph_init(g, 0);
  g->nvertices = 10;

  insert_edge(g, 1, 2, g->directed);
  insert_edge(g, 1, 3, g->directed);
  insert_edge(g, 2, 3, g->directed);
  insert_edge(g, 3, 4, g->directed);
  insert_edge(g, 4, 1, g->directed);
  insert_edge(g, 4, 2, g->directed);
  insert_edge(g, 5, 2, g->directed);
}

int main(void) {
  graph G;
  // G = malloc(sizeof(graph));
  // graph_init(&G, 0);
  // rintf("nv: %d - ne: %d - nd: %d\n", G.nvertices, G.nedges, G.directed);
  //  read_graph(&G, 1);
  create_small_graph(&G);
  print_graph(&G);

  return 0;
}
