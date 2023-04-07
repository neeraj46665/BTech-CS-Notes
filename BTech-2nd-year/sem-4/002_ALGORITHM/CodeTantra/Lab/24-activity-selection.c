#include <stdio.h>

#include <stdlib.h>

struct Activity {
  int start;
  int finish;
};
int compare(const void * a,
  const void * b) {
  return (((struct Activity * ) a) -> finish - ((struct Activity * ) b) -> finish);
}
void printMaxActivities(struct Activity arr[], int n) {
  qsort(arr, n, sizeof(arr[0]), compare);
  int i = 0;
  printf("The following activities are selected: \n");
  printf("%d %d\n", arr[i].start, arr[i].finish);
  for (int j = 1; j < n; j++) {
    if (arr[j].start >= arr[i].finish) {
      printf("%d %d\n", arr[j].start, arr[j].finish);
      i = j;
    }
  }
}
int main() {
  int n;
  printf("Enter the number of activities: ");
  scanf("%d", & n);
  struct Activity arr[n];
  printf("Enter the start and finish times of each activity: \n");
  for (int i = 0; i < n; i++) {
    scanf("%d%d", & arr[i].start, & arr[i].finish);
  }
  printMaxActivities(arr, n);
  return 0;
}