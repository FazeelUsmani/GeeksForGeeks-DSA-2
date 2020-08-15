void toh(int N, int from, int to, int aux, long long &moves) {
if(N==0) return;
moves += 1;
toh(N-1, from, aux, to, moves);
cout << "move disk " << N << " from rod " << from << " to rod " << to << "\n";
toh(N-1, aux, to, from, moves);
}
