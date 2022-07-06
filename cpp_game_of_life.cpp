#include <iostream>
#include <stdlib.h>
#include <ctime>
#include <fstream>

int value_x_y(int** board,int x,int y){
	return board[x][y];
} 

int sum_neighbors(int** board, int r, int c) {
	int sum = 0;
	for(int i = r-1; i < r+2; i++) {
		for(int j = c-1; j < c+2; j++) {
			if((i != r) || (j != c)) {
				sum += board[i][j];			
			}
		}
	}
	return sum;
}

void tick(int** board, int n) {
	int** board_out = new int*[n];
	for(int i = 0; i < n; i++) {
		board_out[i] = new int[n];
	}
	

	//set border to be 0
	for(int x = 0; x < n; x++) { 
		board_out[0][x] = 0;
		board_out[n-1][x] = 0;
		board_out[x][0] = 0;
		board_out[x][n-1] = 0;
	}

	//set non-borders
	for(int i = 1; i < n-1; i++) {
		for(int j = 1; j < n-1; j++) {
			if(board[i][j]) {
				//alive
				if(sum_neighbors(board, i, j)==2 || sum_neighbors(board, i, j)==3){
					board_out[i][j] = 1;
				}
				else {
					board_out[i][j] = 0;
				}
			}		
			else {
				//dead
				if(sum_neighbors(board, i, j)==3){
					board_out[i][j] = 1;
				}
				else {
					board_out[i][j] = 0;
				}
			}
		}
		
	}

	for(int i = 0; i < n; i++){
		for(int j = 0; j < n; j++) {
			board[i][j] = board_out[i][j];
		}
	}
	for(int i = 0; i < n; i++) {
		delete [] board_out[i];
	}
	delete [] board_out;

	
}

void print_matrix(int** matrix, int dim) {
	for(int i = 0; i < dim; i++){
		for(int j = 0; j < dim; j++) {
			std::cout<<matrix[i][j]<<" ";
		}
		std::cout<<"\n";
	}
}

void write_matrix_to_file(int** matrix, int dim, int evolution) {
	std::ofstream myfile;
	myfile.open("evolution"+std::to_string(evolution)+".txt");
	for(int i = 0; i < dim; i++) {
		for(int j = 0; j < dim; j++) {
			myfile << matrix[i][j] << "\n";
		}
	}
}




int main(int argc, char* argv[]) {
	srand((unsigned) time(0));
	int n = atoi(argv[1]);
	int rounds = atoi(argv[2]);
	
	//creates empty board
	int** board = new int*[n];
	for(int i = 0; i < n; i++){
		board[i] = new int[n];
	}
	//initializes board to random binary states
	/*
	for(int i = 0; i < n; i++){
		for(int j = 0; j < n; j++){
			board[i][j] = rand() % 2;
		}
	}
	*/
	//initialize test board
	std::ifstream inFile;
	inFile.open("test_board.board");
	int* test_board = new int[100*100];
	for(int i = 0; i < n*n; i++) {
		inFile >> test_board[i];
	}

	for(int i = 0; i < n; i++){
		for(int j = 0; j < n; j++){
			board[i][j] = test_board[i*n+j];
		}
	}
	delete[] test_board;

	//kill border
	for(int i = 0; i < n; i++){
		board[0][i]=0;
		board[n-1][i]=0;
		board[i][0]=0;
		board[i][n-1]=0;
	}
	write_matrix_to_file(board, n, 0);

	//runs r rounds and prints each board
	std::ofstream paramfile;
	paramfile.open("params.txt");
	paramfile << n;
	paramfile << std::endl;
	paramfile << rounds+1;//total number of states

	for(int r = 0; r < rounds; r++) {
		tick(board, n);
		write_matrix_to_file(board, n, r+1);	
	}

	
	
	

	for(int i = 0; i < n; i++) {
		delete [] board[i];
	}
	delete[] board;
	return 0;
}	
