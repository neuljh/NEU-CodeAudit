#include <stdio.h>
#include <stdlib.h>
void insert_sort(int k[],int n) {
	int i, j;
	int temp;
	for (i = 1; i < n; i++) {
		temp = k[i];
		for (j = i - 1; j >= 0; j--) {
			if (temp > k[j])
				break;
			k[j + 1] = k[j];
		}
		k[j+1] = temp;
	}
}
void bin_insert_sort(int k[], int n) {
	int i, j,left,right,mid;
	int temp;
	for (i = 1; i < n; i++) {
		temp = k[i];
		left = 0;  /*��ǰ����ĳ��ȣ�i*/
		right = i - 1;
		while (left <= right) {  /* ���ڱ�Ҫ�Ŀ��Ա�֤leftΪ��ȷ�Ĳ���λ�� */
			mid = (left + right) / 2;
			if (k[mid] < temp) 
				left = mid + 1;
			else
				right = mid - 1;
		}
		/*left����Ҫ�����λ��*/
		for (j = i ; j > left; j--)
			k[j] = k[j-1];
		k[left] = temp;
	}
}
void select_sort(int k[],int n) {
	int i, j;
	int minIndex,temp;
	for (i = 0; i < n-1; i++) {
		minIndex = i;
		for (j = i+1; j < n; j++) {
			if (k[j] < k[minIndex]) {
				minIndex = j;
			}
		}
		/*��ȡ��index��δ����Ĳ��ֵ�һ��Ԫ�ؽ���λ��*/
		if (minIndex != i) {
			temp = k[i];
			k[i] = k[minIndex];
			k[minIndex] = temp;
		}
	}
}
void bubble_sort(int k[], int n) {
	int i, j, temp;
	int flag=0;
	for (i = 0; i < n; i++) {
		for (j = n - 1; j > i; j--) {
			flag = 0;//��ʼ���ò����ڽ�������
			if (k[j] < k[j - 1]) {
				temp = k[j];
				k[j] = k[j - 1];
				k[j - 1] = temp;
				flag = 1;//���ڽ�������
			}
		}
		if (flag == 0)
			break;
	}
		
}
void shell_sort(int k[], int n) {
	int i, j, temp,flag;
	int gap = n;
	while (gap > 1) {
		gap = gap / 2;
		flag = 0;
		for (i = 0; i < n-gap; i++) {
			j = i + gap;
			if (k[j] < k[i]) {
				temp = k[j];
				k[j] = k[i];
				k[i] = temp;
				flag = 1;
			}
		}
		if (!flag)
			break;
	}
}

void swap(int* a, int *b) {
	int temp = *a;
	*a = *b;
	*b = temp;
}
//����������Ϊ�ָ��ֵ
void Quick(int k[], int left, int right) {
	int i, j;
	if (left >= right) 
		return;
	i = left;
	j = right+1;
	while (1) {
		//Ѱ����˴���standIndex��Ԫ��
		do i++;
		while (k[i] < k[left]);
		do j--;
		while (k[j] > k[left]);
		if (i < j) {
			swap(&k[i], &k[j]);
		}

		else break;
	}
	swap(&k[left], &k[j]); //����׼Ԫ��������ҵ�λ�ý���
	Quick(k, left, j - 1);
	Quick(k, j + 1, right);
}

void quick_sort(int k[], int n) {
	Quick(k, 0, n-1);//ע����Ҫ����n-1�Ҷ˵�λ��
}
void quick_sort_NonRecursive(int k[], int left, int right) {
	// Create a stack for storing partition indexes
	int* stack = (int*)calloc(right - left + 1, sizeof(int));
	int top = -1;

	// Push initial values of left and right to the stack
	stack[++top] = left;
	stack[++top] = right;

	// Run the loop until the stack is empty
	while (top >= 0) {
		// Pop right and left
		right = stack[top--];
		left = stack[top--];

		// Set pivot element at its correct position
		int i = left, j = right + 1;
		while (1) {
			do {
				i++;
			} while (k[i] < k[left]);
			do {
				j--;
			} while (k[j] > k[left]);
			if (i < j) {
				swap(&k[i], &k[j]);
			}
			else {
				break;
			}
		}
		swap(&k[left], &k[j]);

		// If there are elements on the left side of the pivot, push left side to the stack
		if (j - 1 > left) {
			stack[++top] = left;
			stack[++top] = j - 1;
		}

		// If there are elements on the right side of the pivot, push right side to the stack
		if (j + 1 < right) {
			stack[++top] = j + 1;
			stack[++top] = right;
		}
	}
}
void heap_adjust(int k[],int i,int n) {
	//�����ΪԪ�ص���������Ҫ+1ת��Ϊϵ��,����indexΪi�Ľڵ�
	int j;
	int temp;

	
	temp = k[i-1];
	j = 2 * i;//jΪλ�÷�����
	while (j <= n) {
		if (j < n && k[j-1] < k[j]) //�ж�λ��j ��j+1��С
			j++;//��ȡ left right�нϴ�ֵ��index
		if (temp >= k[j-1]) 
			break;
		k[j / 2 -1] = k[j-1];//���ڵ㸳ֵ
		j = 2 * j;//��ʼ��һ��ѭ��,�жϽ�������������Ƿ�temp������
	}
	k[j / 2 -1] = temp;
}
void heap_sort(int k[], int n) {
	int i;
	int temp;
	for (i = n / 2; i >= 1; i--) {
		heap_adjust(k, i, n);
	}
	for (i = n - 1; i > 0; i--) {
		swap(&k[i], &k[0]);// i�ڵ�洢��ǰ����Ԫ��,ע������
		heap_adjust(k, 1, i);
	}
}



void print_k(int k[],int n) {
	for (int i = 0; i < n; i++)
		printf("%d ", k[i]);
	printf("\n");
}
//
//int main() {
//	int k[] = { 49,38,65,97,76,12,27,49 };
//	int len = sizeof(k)/sizeof(int);
//	//12 27 38 49 49 65 76 97
//	//insert_sort(k, len);
//	//bin_insert_sort(k, len);
//	//select_sort(k, len);
//	//bubble_sort(k, len);
//	//shell_sort(k, len);
//	//quick_sort(k, len);
//	quick_sort_NonRecursive(k, 0,len-1);
//	print_k(k, len);
//}