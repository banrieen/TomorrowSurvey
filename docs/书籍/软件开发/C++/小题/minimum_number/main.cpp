#include <iostream>
#include <time.h>
#include <stdlib.h>
#include <stdio.h>
#include "find_main.h"
#include "output_all.h"
//using namespace std;

int main()
{
  //  cout << "Hello world!" << endl;
    srand(time(NULL));
    const unsigned MOD = 100,SZ = rand() % MOD;
    unsigned* arr = (unsigned*)malloc(SZ * sizeof(SZ) );
    unsigned k = 1;
    printf("���ɵ����������Ϊ\��%d \n",SZ);
    for(;k<SZ;++k)
      arr[k] = rand();
    output_all(arr,SZ);  //��ӡ���������

    unsigned min = find_main(arr,SZ);
    if(0 != SZ)
       printf("minimum in all; %d\n",arr[min]);

    free(arr);
    system("PAUSE");


    return 0;
}
