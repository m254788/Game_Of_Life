#include <iostream>
#include <fstream>

int main(int argc, char* argv[]){
	std::ifstream inFile;
	inFile.open("test_board.txt");
	int* test_board = new int[100*100];
	for(int i = 0; i < 100*100; i++){
		inFile >> test_board[i];
	}
	inFile.close();
	for(int i = 0; i < 100; i++){
		std::cout<<test_board[i];
	}
	return 0;
}
