#include <stdlib.h>

int main(int argc, char* argv[]){
    const char command[20] = "python ./console.py";
    system(&command);
    return 0;
}