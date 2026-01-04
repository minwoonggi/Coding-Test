import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(bf.readLine());
        int[] arr = new int[n];
        int[] aswr = new int[n];

        StringTokenizer stringTokenizer = new StringTokenizer(bf.readLine());
        for(int j=0;j<n;j++) {
            arr[j] = Integer.parseInt(stringTokenizer.nextToken());
        }



        int cnt =0;
        for(int i=0;i<n;i++){
            int num=0;
            for(int j=0;j<n;j++){
                if(arr[j]==0){
                    num = j;
                    aswr[cnt] = j+1;
                    cnt++;
                    break;
                }
            }
            for(int j=0;j<=num;j++){
                arr[j]-=1;
            }
        }

        for(int i=0;i<n;i++){
            System.out.print(aswr[i]+" ");
        }
    }
}