#define ElemType int

int a[6][6] = {
	{15,0,0,22,0,-15},
	{0,11,3,0,0,0},
	{0,0,0,-6,0,0},
	{0,0,0,0,0,0},
	{91,0,0,0,0,0},
	{0,0,28,0,0,0}
};

/*
 @description: m��n�е�ϡ�����ת��Ϊ��Ԫ��
 ��ά������Ϊ��������ά
 @return : none
*/
void Sparse_matrix_convert_Triples(const ElemType** matrix,int height,int width,ElemType result[][3]) {
	int i, j,sum=0;
	result[0][0] = height;
	result[0][1] = width;
	for (i = 0; i < height; i++) {
		for (j = 0; j < width; j++) {
			if (matrix[i][j] != 0) {
				sum++;
				result[sum][0] = i;
				result[sum][1] = j;
				result[sum][2] = matrix[i][j];
			}
		}
	}
	result[0][2] = sum;
}
