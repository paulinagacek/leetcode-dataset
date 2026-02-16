int uniquePaths(int m, int n){
    
    // make a 2D array of m x n
    int **res = calloc(m, sizeof(int*));
    for(int i=0; i < m; i++) *(res + i) = calloc(n, sizeof(int));
    
    // set the values in top row and left column to 1
    for(int i=0; i < m; i++) res[i][0] = 1;
    for(int i=0; i < n; i++) res[0][i] = 1;
    
    // counting each value
    for(int i=1; i < m; i++){
        for(int j=1; j < n; j++)
            res[i][j] = res[i - 1][j] + res[i][j - 1];
    }
    int ans = res[m - 1][n - 1];
    free(res);
    return ans;
    
}
