#include "graph.h"

int processed[MAXV + 1];
int discovered[MAXV + 1];
int parent[MAXV + 1];

int entry_time[MAXV + 1];
int exit_time[MAXV + 1];
int time;

int finished = 0;

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

edgenode_ptr edgenode_init() {
  edgenode_ptr p;
  p = malloc(sizeof(edgenode));
  return p;
}

void insert_edge(graph_ptr g, int x, int y, int directed) {
  edgenode_ptr p;
  p = edgenode_init();

  p->weight = 0;
  p->val = y;
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
      printf(" %d", p->val);
      p = p->next;
    }
    printf(" degree: %d", g->degree[i]);
    printf("\n");
  }
}

void init_graph_search(graph_ptr g) {
  int i;

  time = 0;

  for (i = 0; i <= g->nvertices; i++) {
    processed[i] = FALSE;
    discovered[i] = FALSE;
    parent[i] = -1;
  }
}


void bfs(graph_ptr g, int start) {
  queue q;
  // int v;
  edgenode_ptr neighbours;

  init_queue(&q);
  enqueue(&q, start);
  discovered[start] = TRUE;

  /**
  *
  * while len(q):
  *   vrtx = q.pop(0)
  *   discovered.add(vrtx)
  *   for x in grah.adjacdencylsit[vrtx]:
  *     if x not in processed:
  *       process(vrtx, x)
  *     if x not in discovered:
  *       discovered.add(x)
  *       q.append(x)
  **/
  while (!empty_queue(&q)) {
    int vrtx = dequeue(&q);
    printf("%d", vrtx);
    printf(" -> ");
    processed_vertex_early(vrtx);
    processed[vrtx] = TRUE;// not compulsary to mark it processed here, we could do that at the end of the outer loop
    neighbours = g->edges[vrtx]; // get the list of the vrtx connections
    // for neighbour in graph.adjacency_list[vrtx]
    while (neighbours != NULL) {
      int neighbour = neighbours->val;
      if ((!processed[neighbour]) || g->directed) {
        process_edge(vrtx, neighbour);
      }

      if (!discovered[neighbour]) {
        enqueue(&q, neighbour);
        discovered[neighbour] = vrtx;
        parent[neighbour] = vrtx;
      }
      neighbours = neighbours->next;
    }
    process_vertex_late(vrtx);
  }
}

void create_small_graph(graph_ptr g) {
  int m;
  graph_init(g, 0);
  g->nvertices = 20;

  insert_edge(g, 1, 2, g->directed);
  insert_edge(g, 1, 3, g->directed);
  insert_edge(g, 2, 3, g->directed);
  insert_edge(g, 3, 4, g->directed);
  insert_edge(g, 4, 1, g->directed);
  insert_edge(g, 4, 2, g->directed);
  insert_edge(g, 5, 2, g->directed);
  insert_edge(g, 5, 10, g->directed);
  insert_edge(g, 10, 20, g->directed);
}

void find_path(int start, int end, int parents[]){
  if((start == end) || (end == -1)){
    printf("\n%d", start);
  }else {
    find_path(start, parents[end], parents);
    printf(" %d", end);
  }
}
