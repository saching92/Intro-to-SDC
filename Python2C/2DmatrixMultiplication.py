//TODO: Write a function that receives two integer matrices and outputs
// the sum of the two matrices. Then in your main() function, input a few
// examples to check your solution. Output the results of your function to 
// cout. You could even write a separate function that prints an arbitrarily 
// sized matric to cout.

#include<vector>
#include<iostream>

using namespace std;

int main()
{
    
    vector<vector <int> >twodvector1;
    vector<int>singlerow1(3,2);
    
    vector<vector <int> >twodvector2;
    vector<int>singlerow2(3,2);
    
    for(int i=0; i<3;i++)
    {
        
        twodvector.push_back(singlerow);
        twodvector1.push_back(singlerow1);
    }
    
    
    for(int row=0; row<twodvector.size;row++)
    {
        for(int col=0,col<twodvector[0].size; col++)
        {
            cout<<twodvector1[row][col]+twodvector2[row][col]
        }
        cout<<endl;
    }
    
    return 0;
    
}
