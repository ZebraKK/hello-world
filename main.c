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

