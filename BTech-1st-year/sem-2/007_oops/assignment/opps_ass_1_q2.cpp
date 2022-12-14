#include <bits/stdc++.h>
using namespace std;
class Animal{
    private:
        int age;
    protected:
        int id;
    public:
        string name;
        int getAge(){
            return age;
        }
        void Setage(int a){
            age=a;
        }
        int getId(){
            return id;
        }
        void setId(int i){
            id=i;;
        }
};
int main() {
    Animal a1;
    a1.name="neeraj";
    a1.setId(1234);
    a1.setId(4);
    cout<<"name is :"<<a1.name<<endl;
    cout<<"age is : "<<a1.getAge()<<endl;
    cout<<"id is : "<<a1.getId()<<endl;
    return 0;
}