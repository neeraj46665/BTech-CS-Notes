#include<stdio.h>
#include<stdlib.h>

int maximum(int a, int b) {
  return (a > b) ? a : b;
}

int longestCommonSubsequence(char * A, char * B, int m, int n, int ** Table) {
  if (m == 0 || n == 0)
    return 0;
  if (A[m - 1] == B[n - 1])
    return Table[m][n] = 1 + longestCommonSubsequence(A, B, m - 1, n - 1,
      Table);
  if (Table[m][n] != -1) {
    return Table[m][n];
  }
  return Table[m][n] = maximum(longestCommonSubsequence(A, B, m, n - 1, Table),
    longestCommonSubsequence(A, B, m - 1, n, Table));
}