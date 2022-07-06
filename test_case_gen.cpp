#include <fstream>
#include <ctime>

int main(int argc, char* argv[]) {
	srand((unsigned) time(0));
	std::ofstream myfile;
	myfile.open("test_board.txt");
	for(int i = 0; i < 100*100; i++){
		myfile << rand()%2 << "\n";
	}
}
