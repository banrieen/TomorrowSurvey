#include "pch.h"
#include "BasementAlgorithms.h"

SortAndQuery::SortAndQuery()
{
}

SortAndQuery::~SortAndQuery()
{
}


void SortAndQuery::display(int array[], int len)
{
	int k;
	for (k = 0; k < len; k++)
		std::cout << array[k] << ",";
}

void quickSort(int s[], int l, int r)
{
	if (l < r)
	{
		int i = l, j = r, x = s[l];
		while (i < j)
		{
			while (i < j && s[j] >= x) // ���������ҵ�һ��С��x����
				j--;
			if (i < j)
				s[i++] = s[j];
			while (i < j && s[i] < x) // ���������ҵ�һ�����ڵ���x����
				i++;
			if (i < j)
				s[j--] = s[i];
		}
		s[i] = x;
		quickSort(s, l, i - 1); // �ݹ����
		quickSort(s, i + 1, r);
	}
}


void merge(int a[], int low, int mid, int high) {
	// subarray1 = a[low..mid], subarray2 = a[mid+1..high], both sorted
	// �鲢����
	int N = high - low + 1;
	int* b = new int[N]; 
	int left = low, right = mid + 1, bIdx = 0;
	while (left <= mid && right <= high) // �鲢
		b[bIdx++] = (a[left] <= a[right]) ? a[left++] : a[right++];
	while (left <= mid) b[bIdx++] = a[left++]; // leftover, if any
	while (right <= high) b[bIdx++] = a[right++]; // leftover, if any
	for (int k = 0; k < N; k++) a[low + k] = b[k]; // copy back
}

void mergeSort(int a[], int low, int high) {
	// Ҫ����������� a[low..high]
	if (low < high) { // base case: low >= high (0 or 1 item)
		int mid = (low + high) / 2;
		mergeSort(a, low, mid); // �ֳ�һ��

		mergeSort(a, mid + 1, high); // �ݹ�ؽ���������
		merge(a, low, mid, high); // ���: �鲢�ӳ���
	}
}


//�����ӷ��������׼λ��
int Partition(int arr[], int nLower, int nUpper)
{
	int pivot = arr[nLower]; //ȡ��һ����¼Ϊ��׼��¼��
	int nLeft = nLower + 1; //��1 ��pivot ���������Ƚϣ�
	int nRight = nUpper;
	int temp;
	do {
		while (nLeft <= nRight && arr[nLeft] <= pivot)  //��nLeft������֪���ҵ�pivot���±�Ϊֹ��
			nLeft++;
		while (nLeft <= nRight && arr[nRight] > pivot)   //��
			nRight--;
		//R[nLeft,nRight]����ĳ���(Ԫ����)����1ʱ������R[nLeft]��R[nRight]
		if (nLeft < nRight)
		{
			temp = arr[nLeft];
			arr[nLeft] = arr[nRight];
			arr[nRight] = temp;
			nLeft++;
			nRight--;
		}
	} while (nLeft < nRight);  //��nLeft==nRightʱ��ֹͣѭ����
	//�ѻ�׼��¼pivot�ŵ���ȷλ�ã���nLeft��nRightͬʱָ���λ�ã�
	temp = arr[nLower];
	arr[nLower] = arr[nLeft];
	arr[nRight] = temp;
	return nRight;

}


int SortAndQuery::QuickSort(int arr[], int nLower, int nUpper)
{
	int pivotpos;  //��׼�±ꣻ
	if (nLower < nUpper)  //�������䳤�ȴ���1ʱ������
	{
		pivotpos = Partition(arr, nLower, nUpper); //����������֪����׼�±꣬��QuictSort�Ĺؼ�����
		QuickSort(arr, nLower, pivotpos + 1);      //��������ݹ�����
		QuickSort(arr, pivotpos + 1, nUpper);      //��������ݹ�����
	}
	return 0;
}
