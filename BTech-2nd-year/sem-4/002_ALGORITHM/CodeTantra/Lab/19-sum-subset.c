#include<stdio.h>

#define TRUE 1
#define FALSE 0
void sumset(int i, int wt, int total);
int inc[50], w[50], sum, n;
int subset(int i, int wt, int total) {
  return (wt == sum);

}
void main() {
  int i, j, n, temp, total = 0;
  printf("Enter number of elements in the subset: ");
  scanf("%d", & n);
  printf("Enter %d numbers to the set: ", n);
  for (i = 0; i < n; i++) {
    scanf("%d", & w[i]);
    total += w[i];

  }
  printf("Enter the input number to find subsets: ");
  scanf("%d", & sum);
  for (i = 0; i <= n; i++)
    for (j = 0; j < n - 1; j++)
      if (w[j] > w[j + 1]) {
        temp = w[j];
        w[j] = w[j + 1];
        w[j + 1] = temp;
      }
  if (total < sum || w[0] > sum)
    printf("Subset construction is not possible\n");
  else {
    for (i = 0; i < n; i++)
      inc[i] = FALSE;
    printf("The solution is: \n");
    sumset(-1, 0, total);
  }
}

void sumset(int i, int wt, int total) {
  int j;
  if (subset(i, wt, total)) {

    printf("{");
    for (j = 0; j <= i; j++) {
      if (inc[j] == TRUE) {
        printf("%d ", w[j]);
      }
    }
    printf("}\n");
  } else {
    if (wt + w[i + 1] <= sum) {
      inc[i + 1] = TRUE;
      sumset(i + 1, wt + w[i + 1], total - w[i + 1]);
    }
    if (wt + total - w[i + 1] >= sum) {
      inc[i + 1] = FALSE;
      sumset(i + 1, wt, total - w[i + 1]);
    }

  }
}