#include<iostream>

using namespace std;


class minHeap{
    
    int *arr;
    int capacity;
    int size;
    public:
    minHeap(int capacity){
        arr = new int[capacity];
        this->capacity = capacity;
        size = 0;
    }

    int left(int i ){
        return 2*i+1;
    }
    int right(int i ){
        return 2*i+2;
    }
    int parent(int i){
        if(i==0)
            return 0;
        return (i-1)/2;
    }

    void insert(int n){
        if (size == capacity) return;
        size ++;
        arr[size-1] = n;
        int i = size-1;
        while(i>0 and arr[parent(i)] > arr[i]){
            swap(arr[i],arr[parent(i)]);
            i = parent(i);
        }
    }    
    
};

int main(){
    return 0;
}