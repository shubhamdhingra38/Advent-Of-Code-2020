import java.io.*;
import java.util.*;

public class AOC5 {

    
/*

  ____   _             _      _                         ____   _      _                           
 / ___| | |__   _   _ | |__  | |__    __ _  _ __ ___   |  _ \ | |__  (_) _ __    __ _  _ __  __ _ 
 \___ \ | '_ \ | | | || '_ \ | '_ \  / _` || '_ ` _ \  | | | || '_ \ | || '_ \  / _` || '__|/ _` |
  ___) || | | || |_| || |_) || | | || (_| || | | | | | | |_| || | | || || | | || (_| || |  | (_| |
 |____/ |_| |_| \__,_||_.__/ |_| |_| \__,_||_| |_| |_| |____/ |_| |_||_||_| |_| \__, ||_|   \__,_|
                                                                                |___/             

*/

    //---------------------------------- STARTS HERE ----------------------------------
    static int getSeatID(String s){
        int row, col;
        int rowStart, rowEnd;
        rowStart=0; rowEnd=127;
        for(int i=0; i<7; ++i){
            char c=s.charAt(i);
            int mid=(rowStart+rowEnd)/2;
            if(c=='F'){
                rowEnd=mid;
            }
            else{
                rowStart=mid+1;
            }
        }
        row=rowStart;
        int colStart, colEnd;
        colStart=0; colEnd=7;
        for(int i=7; i<10; ++i){
            char c=s.charAt(i);
            int mid=(colStart+colEnd)/2;
            if(c=='L'){
                colEnd=mid;
            }
            else{
                colStart=mid+1;
            }
        }
        col=colStart;
        return row*8+col;
    }

    public static void main(String[] args) throws FileNotFoundException {
        File myFile = new File("/Users/shubham/IdeaProjects/Code/AOC/src/day5.txt");
        Scanner sc=new Scanner(myFile);
        int mx=Integer.MIN_VALUE;
        ArrayList<Integer> seatIDs=new ArrayList<>();
        for(int i=0; i<128; ++i){
            for(int j=0; j<8; ++j){
                seatIDs.add(i*8+j);
            }
        }
        HashSet<Integer> gotIDS=new HashSet<>();
        while(sc.hasNextLine()){
            String s=sc.nextLine();
            int id=getSeatID(s);
            gotIDS.add(id);
        }
        HashSet<Integer> ignore=new HashSet<>();
        for(int i=0; i<8; ++i){
            ignore.add(i);
            ignore.add(127*8+i);
        }
        System.out.println();
        for(int id: seatIDs){
            if(!gotIDS.contains(id) && gotIDS.contains(id+1) && gotIDS.contains(id-1)){
                System.out.println(id);
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

