int selection_sort(int * a, int n) {
	for (int i = 0; i < n - 1; i++) {
		int k = i;
		for (int j = i + 1; j < n; j++) {
			if (a[j] < a[k])
				k = j;
		}
		if (a[k] < a[i]) {
			int temp = a[i];
			a[i] = a[k];
			a[k] = temp;
		}
	}
	return 0;
}
