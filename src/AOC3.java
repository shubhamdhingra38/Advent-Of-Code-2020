import java.io.*;
import java.util.*;

public class AOC3 {

    
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
        File myFile = new File("/Users/shubham/IdeaProjects/Code/AOC/src/day3.txt");
        Scanner sc=new Scanner(myFile);
        ArrayList<String> arr=new ArrayList<>();
        String s="";
        while(sc.hasNextLine()){
            s=sc.nextLine();
            arr.add(s);
        }
        char[][] mat=new char[arr.size()][s.length()];
        for(int i=0; i<arr.size(); ++i){
            mat[i]=arr.get(i).toCharArray();
        }
        int cnt=0;
        int posX, posY;
        posX=posY=0;
        while(true){
            posX+=2;
            posY++;
            if(posX>=mat.length){
                break;
            }
            if(posY>=mat[0].length){
                posY%=mat[0].length;
            }
            if(mat[posX][posY]=='#'){
                cnt++;
            }
        }
        System.out.println("RESULT IS " + cnt);
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

