#include <bits/stdc++.h>
using namespace std;

int main() {
    //while
    while(1){
        cout<<"1.one"<<endl;
        cout<<"2.two"<<endl;
        cout<<"3.three"<<endl;
        int n;
        cin>>n;
        //switch
        switch (n)
        {
        case 1:
        cout<<"one\n";
            break;

        case 2:
        cout<<"two\n";
            break;

        case 4:
        cout<<"three\n";
            break;
        default:
            break;
        }
        //for
        for(int i=0;i<1;i++){
            if(n==1){
                cout<<"hello one "<<endl;
            }
            else if(n==2){
                cout<<"hello two"<<endl;
            }
            else if(n==3){
                cout<<"hello three"<<endl;
            }
            else{
                cout<<"hello world"<<endl;
            }
        }
        char ch;
        cout<<"do you want to continue(y/n):";
        cin>>ch;
        //if
        if(ch=='n' || ch=='N'){
            break;
        }
    }
    return 0;
}