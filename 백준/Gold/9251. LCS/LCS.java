import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));

        String s1 = bf.readLine();
        String s2 = bf.readLine();

        char[] arr1 = s1.toCharArray();
        char[] arr2 = s2.toCharArray();

        int[][] arr= new int[arr1.length+1][arr2.length+1];
       
        for(int i=1;i<=arr1.length;i++){
            for(int j=1; j<=arr2.length; j++){
                if(arr1[i-1] == arr2[j-1]){
                    arr[i][j] = arr[i-1][j-1]+1;
                }else{
                   int max = 0;
                   max = Math.max(arr[i-1][j],arr[i][j-1]);
                   arr[i][j] = max;
                }
            }
        }
        System.out.println(arr[arr1.length][arr2.length]);
    }
}