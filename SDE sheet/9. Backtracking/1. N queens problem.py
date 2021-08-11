"""

The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.
Given an integer n, print all distinct solutions to the n-queens puzzle.
Each solution contains distinct board configurations of the n-queens’ placement,
where the solutions are a permutation of [1,2,3..n] in increasing order
here the number in the ith place denotes that the ith-column queen is placed in the row with that number.
For eg below figure represents a chessboard [3 1 4 2].

commented solution in c++ as python solution was not working
"""

"""
#include<bits/stdc++.h>
using namespace std;

bool isSafe(vector<vector<int> > &board, int row, int col, int n){
    //Checking in the same row
    for(int i=0; i<col; i++)
    {
        if(board[row][i] == 1)
            return false;
    }
    //Checking upper left diagonal
    for(int i=row, j=col; i>=0 && j>=0; i--, j--)
    {
        if(board[i][j] == 1)
            return false;
    }
    //Checking lower left diagonal
    for(int i=row, j=col; i<n && j>=0; i++, j--)
    {
        if(board[i][j] == 1)
            return false;
    }
    return true;
}

void nQueen(vector<vector<int> > &board, vector<vector<int> > &res, int col, int n){
    if(col >= n)
    {
        vector<int> temp(n,0);
        for(int i=0; i<n; i++)
        {
            for(int j=0; j<n; j++)
            {
                if(board[j][i] == 1)
                    temp[i] = j+1;
            }
        }
        res.push_back(temp);
    }
    
    for(int i=0; i<n; i++)
    {
        if(isSafe(board,i,col,n))
        {
            board[i][col] = 1;                  //Setting current cell as Queen
            nQueen(board, res, col+1, n);       //Moving on to the next column
            board[i][col] = 0;                  //Setting the original value and backtracking
        }
    }
}

int main()
{
	int t;
	cin >> t;
	while(t--)
	{
	    int n;
	    cin >> n;
	    vector<vector<int> > board(n, vector<int> (n,0));
	    vector<vector<int> > res;
	    nQueen(board, res, 0, n);
	    int m = res.size();
	    if(m==0)
	    {
	        cout<<-1<<endl;
	        continue;
	    }
	    for(int i=0; i<m; i++)
	    {
	        cout<<'[';
	        for(int j=0; j<n; j++)
	        {
                cout<<res[i][j]<<" ";
	        }
	        cout<<']'<<' ';
	    }
	    cout<<endl;
	}
	return 0;
}

TC = o(2^n)
Sc = o(n*n)
"""