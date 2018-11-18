public class Solution {
    public double FindMedianSortedArrays(int[] nums1, int[] nums2) {
        int sum = 0, count = 0;

        int[] all_nums = nums1.Concat(nums2).ToArray();
        
        /*
        for (int i = 0; i < all_nums.Length - 1; i++) {
            for (int j = i + 1; j < all_nums.Length; j++) {
                if (all_nums[i] > all_nums[j]) {
                    int temp = all_nums[i];
                    all_nums[i] = all_nums[j];
                    all_nums[j] = temp;
                }
            }
        }
        */
        sort(all_nums);
        
        if (all_nums.Length % 2 == 1){
            return(all_nums[all_nums.Length / 2]);
        }
        else{
            return((double)(all_nums[all_nums.Length/2 - 1] + all_nums[all_nums.Length/2])/ 2);
        }
        
        /*
        8   012 34 567
        9   0123 4 5678
        */
    }

    public int pivot(int[] a, int i, int j)
    {
        int k = i + 1;
        
        while ( k <= j && a[i] == a[k])
            k++;

        if(k>j)
            return -1;
        if(a[i]>=a[k])
            return i;
        return k;
    }

    public int partition(int[] a,int i,int j,int x)
    {
        int l=i,r=j;

        // 検索が交差するまで繰り返します
        while(l<=r) {

            // 軸要素以上のデータを探します
            while(l<=j && a[l]<x)
                l++;

            // 軸要素未満のデータを探します
            while(r>=i && a[r]>=x)
                r--;

            if ( l > r )
                break;
        
            int t=a[l];
            a[l]=a[r];
            a[r]=t;
            l++;
            r--;
        }
        
        return l;
    }
    
    public void sort(int[] a)
    {
        quickSort(a, 0, a.Length-1);
    }

    public void quickSort(int[] a, int i, int j)
    {
        if ( i == j )
            return;
        
        int p = pivot(a,i,j);

        if ( p != -1 ) {
            int k = partition( a, i, j, a[p] );
            quickSort( a, i, k-1 );
            quickSort( a, k, j );
        }
    }
}

