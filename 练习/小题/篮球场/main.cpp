#include <iostream>

using namespace std;


int main()
{
    cout << "Hello world!" << endl;
    int a, b, c, i,j,k,t;
    b=100;
    c=200;
    t=10;
        for (i=1;i<=t;i++)
    {
        b++;
        c=c-2;
        a = b+c;
    }
    k=a;   //��Сֵ k==290
    j=a;
    for (i=1;i<=t;i++)
    {
        b++;
        c=c-2;
        a = b+c;
     //���������
            while (a-k<0)
            {
                 k--;
              cout<<"   "<<" ";
             }
   // ��ȫ������Ϊ����,KΪ���ֵ

   k=j;

         while (k-(a+10)<=0)
           {
             k++;
             cout<<a<<" ";
            }
   k=j;

  //����������Σ��� | ���Ÿ��� a==k
     cout<<" "<<"|"<<"  ";
         while (k-(a+10)<=0)
           {
             k++;
             cout<<a<<" ";
            }
   k=j;
     cout<<endl;
    }
    return 0;
}
