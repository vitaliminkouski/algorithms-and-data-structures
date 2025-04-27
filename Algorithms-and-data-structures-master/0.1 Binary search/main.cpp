#include <iostream>
#include <algorithm>

int binarySearch(std::vector<int> arr, int lenOfArr, int x){
    int rightIndex=lenOfArr;
    int leftIndex=0;
    int middleIndex;
    while(leftIndex<rightIndex){
        middleIndex=(rightIndex+leftIndex)/2;
        if(arr[middleIndex]==x){
            return 1;
        }
        else if(arr[middleIndex]>x){
            rightIndex=middleIndex;
        } else {
            leftIndex=middleIndex+1;
        }
    }
    return 0;
}

int lowerBound(std::vector<int> arr, int lenOfArr, int x){
    int rightIndex=lenOfArr;
    int leftIndex=0;
    int middleIndex;
    while(leftIndex<rightIndex){
        middleIndex=(leftIndex+rightIndex)/2;
        if(arr[middleIndex]>=x){
            rightIndex=middleIndex;
        } else{
            leftIndex=middleIndex+1;
        }
    }
    return leftIndex;
}

int upperBound(std::vector<int> arr, int lenOfArr, int x){
    int rightIndex=lenOfArr;
    int leftIndex=0;
    int middleIndex;
    while(leftIndex<rightIndex){
        middleIndex=(leftIndex+rightIndex)/2;
        if(arr[middleIndex]>x){
            rightIndex=middleIndex;
        } else{
            leftIndex=middleIndex+1;
        }
    }
    return leftIndex;
}

int main(){
    int lenOfArr;
    std::cin>>lenOfArr;
    std::vector<int> arr(lenOfArr);
    for (int i = 0; i < lenOfArr; i++)
    {
        std::cin>>arr[i];
    }
    int numOfRequests;
    std::cin>>numOfRequests;
    std::vector<int> arrOfRequests(numOfRequests);
    for(int i=0; i<numOfRequests; i++){
        std::cin>>arrOfRequests[i];
    }

 for (int i = 0; i < numOfRequests; i++)
 {
    std::cout<<binarySearch(arr, lenOfArr, arrOfRequests[i])<<" "
             <<lowerBound(arr, lenOfArr, arrOfRequests[i])<<" "
             <<upperBound(arr, lenOfArr, arrOfRequests[i])<<"\n";
 }
 
    
    return 0;
}