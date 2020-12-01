import java.io.*;
import java.util.*;

public class AOC1B {

    
/*

  ____   _             _      _                         ____   _      _                           
 / ___| | |__   _   _ | |__  | |__    __ _  _ __ ___   |  _ \ | |__  (_) _ __    __ _  _ __  __ _ 
 \___ \ | '_ \ | | | || '_ \ | '_ \  / _` || '_ ` _ \  | | | || '_ \ | || '_ \  / _` || '__|/ _` |
  ___) || | | || |_| || |_) || | | || (_| || | | | | | | |_| || | | || || | | || (_| || |  | (_| |
 |____/ |_| |_| \__,_||_.__/ |_| |_| \__,_||_| |_| |_| |____/ |_| |_||_||_| |_| \__, ||_|   \__,_|
                                                                                |___/             

*/

    //---------------------------------- STARTS HERE ----------------------------------

    public static void main(String[] args) throws FileNotFoundException {
        File myFile = new File("src/day1.txt");
        Scanner sc=new Scanner(myFile);
        ArrayList<Integer> arr=new ArrayList<>();
        while(sc.hasNextLine()){
            int ele=Integer.parseInt(sc.nextLine());
            arr.add(ele);
        }
        for(int i=0; i<arr.size(); ++i){
            for(int j=0; j<arr.size(); ++j){
                if(i==j) continue;
                for(int k=0; k<arr.size(); ++k){
                    if(i==k || k==j) continue;
                    if(arr.get(i)+arr.get(j)+arr.get(k)==2020){
                        System.out.println((long)arr.get(i)*arr.get(j)*arr.get(k));
                    }
                }
            }
        }
    }

    //---------------------------------- ENDS HERE ----------------------------------


    static class FastReader {
        BufferedReader br;
        StringTokenizer st;

        public FastReader() {
            br = new BufferedReader(new InputStreamReader(System.in));
        }

        String next() {
            while (st == null || !st.hasMoreElements()) {
                try {
                    st = new StringTokenizer(br.readLine());
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            return st.nextToken();
        }

        int nextInt() {
            return Integer.parseInt(next());
        }

        long nextLong() {
            return Long.parseLong(next());
        }

        double nextDouble() {
            return Double.parseDouble(next());
        }

        String nextLine() {
            String str = "";
            try {
                str = br.readLine();
            } catch (IOException e) {
                e.printStackTrace();
            }
            return str;
        }
    }
}

