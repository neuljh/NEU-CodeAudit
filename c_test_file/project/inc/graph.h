#pragma once
typedef struct edge {
	/*�߽�㶨��*/
	int loaction; //�ýڵ�λ�������е�λ��
	int weight;
	struct edge* next;
}edge;
typedef struct ver {
	int data; //����洢����Ϣ
	edge* next;//��һ���߽��
}ver;

void graph_create_array(int a[][100], int n, int e);
void graph_create_link(ver G[], int n, int e, int edata[][3]);
void graph_link_print(ver G[], int n);
void visit_ver(ver node);
/*
 @description: ������ȱ���
 @param : GΪ����洢���ڽӱ�vΪ�����Ķ��㣬visited��¼�ڵ������Ϣ
*/
void DFS(ver G[], int v, int visited[]);
void graph_dfs(ver G[], int n);
/*
 @description: �������ʹ�õݹ��㷨
 @return : none
*/
void BFS(ver G[], int v, int visited[]);
/*
 @description:��ʹ�õݹ��㷨
 @return : none
*/
void BFS2(ver G[], int v, int visited[]);
void graph_bfs(ver G[], int n);
void prim_minspant(int GE[6][6], int n);
void short_path(int GE[6][6], int n, int head);