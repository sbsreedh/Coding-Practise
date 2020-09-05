#Find threshold
// "static void main" must be defined in a public class.
public class Main {
    public static float findThreshold(int[] nums, int desiredSum) {
        //Sort the array
        //numbers greater than threshold will not change the threshold but the smaller numbers will
        //keep updating threshold if the number < the current threshold;
        float n=nums.length;
        Arrays.sort(nums);
        float threshold=desiredSum/n;
        for(int i=0;i<n;i++) {
            if(nums[i] < threshold) {
                //calculate new threshold and distribute the diff among threshold of remaining numbers
                float diff=threshold-nums[i];
                threshold=threshold+diff/(n-(i+1));
            }
        }
        return threshold;
    }
    public static void main(String[] args) {
        int[] nums=new int[]{2, 1, 5};
        System.out.println(findThreshold(nums, 1));
        System.out.println(findThreshold(nums, 2));
        System.out.println(findThreshold(nums, 6));
        System.out.println(findThreshold(nums, 4));
    }
}

/*-----------------------------------------*/
// // "static void main" must be defined in a public class.
// public class Main {
//     public static void main(String[] args) {
//         int[] inp={2,1,5};
//         int gs=2;
//         int max=0;
//         Arrays.sort(inp);
//         int sum=0;
//         int flag=0;
//         while(sum!=gs)
//         {   flag=0;
//             System.out.println("In while");
//             max=inp[0];sum=0;
//             for(int x:inp)
//             { sum=sum+x;
//               max=x>max?x:max;
//              System.out.println("Check:"+sum+" "+max);
//             }
            
//             for(int x:inp)
//                 if(x!=1)
//                    flag=1;
//             System.out.println(flag);
//            if(flag==0)
//            {        double ans=(double)gs/inp.length;
//                     System.out.println(ans);
//                     return;
//            }
//             if(sum>gs)
//                 for(int i=inp.length-1;i>=0;i--)
//                     if(inp[i]==max)
//                         inp[i]--;
//         }
        
//         System.out.println(max);
//     }
// }
