#include <stdio.h>
#include <stdlib.h>

void main()
{
   printf("hello world \n");
}

//list reverse

typedef struct link
{
    int date;
    struct link *pnext;
}Node;

Node* reverse(Node *list)
{
    Node *p;
    Node *q;

    p=list->pnext;
    list->pnext=NULL;
    
    while(p!=NULL)
    {
        q=p;
        p=p->pnext;
        
        q->pnext=list->pnext;
        list->pnext=q;
    }
    
    return list;
}

// quiksort
int pivortfind(char data[],int,int);
void qquiksort(char data[],int,int);

int pivotfind(char data[],int low, int high)
{
    int pivot=0;

    pivot=data[low];
    while(low<high)
    {
        while(pivot<=data[high])
        {
            --high;
        }
   
        data[low]=data[high];
    
        while(data[low]<=pivot)
        {
            ++low;
        }
       
        data[high]=data[low];
    }
    data[low]=pivot;

    return low;    
}

void qquiksort(char data[], int low, int high)
{
    int pivot;
    
    pivot=pivotfind(data,low,high);

    qquiksort(data,low,pivot-1);
    
    qquiksort(data,pivot+1,high);    

}

//bit-sort


//KMP






