#include<stdio.h>
#include<stdlib.h>
#include<time.h>

int getN(){
  srand(time(NULL));
  int N = rand() % 13 + 1;
  printf("今回はROT%dです\n",*N);
  return N;
}

void rot(int N){
  char cha;
  printf("文字列を入力してください\n");
  while((cha = getchar()) != '\n'){
    if(cha > 0x7a - N){
      cha = cha - 26 + N;
    } else{
      cha += N;
    }
      printf("%c",cha);
  }
}

int main(){
  rot(getN());
  printf("\n");
  return 0;  
}
