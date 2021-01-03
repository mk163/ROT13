#include<stdio.h>
#include<stdlib.h>
#include<time.h>

void getN(int *N){
  srand(time(NULL));
  *N = rand() % 13 + 1;
  printf("今回はN%dです\n",*N);
}

void rot(int *N){
  char cha;
  printf("文字列を入力してください\n");
  while((cha = getchar()) != '\n'){
    if(cha > 0x7a - *N){
      cha = cha - 26 + *N;
    } else{
      cha += *N;
    }
      printf("%c",cha);
  }
}

int main(){
  int N;
  getN(&N);
  rot(&N);
  printf("\n");
  return 0;  
}
