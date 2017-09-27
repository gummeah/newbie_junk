int bin_add(int * a, int * b, int * c, int n ){
    int carry = 0;
    for(int i = n-1; i >= 0; i--){
        c[i+1] = (a[i] + b[i] + carry) % 2;
        carry = (a[i] + b[i] + carry) / 2;
    }
    c[0] = carry; 
    return 0;
}