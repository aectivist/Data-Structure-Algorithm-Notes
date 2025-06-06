class Seq {
    public static int search(int arr[], int N, int x) //search function
    {
        for (int i = 0; i < N; i++) {
            if (arr[i] == x)
                return i;
        }
        return -1;
    }

    // Setup and Output
    public static void main(String args[]) 
    {
        int arr[] = { 2, 3, 4, 10, 40 };
        int x = 10;

        // Function output
        int result = search(arr, arr.length, x);
        if (result == -1)
            System.out.print(
                "Element is not present in array");
        else
            System.out.print("Element is present at index "
                             + result);
    }
}
