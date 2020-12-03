import java.io.*;
import java.util.*;

public class AOC2B {


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
        File myFile = new File("/Users/shubham/IdeaProjects/Code/AOC/src/day2.txt");
        Scanner sc=new Scanner(myFile);
        int cnt=0;
        while(sc.hasNextLine()){
            String line=sc.nextLine();
            StringTokenizer st=new StringTokenizer(line, " ");
            String range=st.nextToken();
            String rule=st.nextToken();
            String pass=st.nextToken();
            StringTokenizer rangeTokenizer=new StringTokenizer(range, "-");
            int min=Integer.parseInt(rangeTokenizer.nextToken());
            int max=Integer.parseInt(rangeTokenizer.nextToken());
            char c=rule.charAt(0);
            boolean f1, f2;
            f1=pass.charAt(min-1)==c;
            f2=pass.charAt(max-1)==c;
            if(f1&&f2){
                continue;
            }
            else if(f1){
                cnt++;
            }
            else if(f2){
                cnt++;
            }
        }
        System.out.println(cnt);
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

