import java.io.*;
import java.util.*;

public class AOC4 {

    
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
        File myFile = new File("/Users/shubham/IdeaProjects/Code/AOC/src/day4.txt");
        Scanner sc=new Scanner(myFile);
        int cnt=0;
        String s="";
        String[] required={"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"};
        HashSet<String> mp=new HashSet<>();
        int i=0;
        while(sc.hasNextLine()){
            i++;
            s=sc.nextLine();
            if(s.length()==0){
                boolean good=true;
                for(String x: required){
                    if(!mp.contains(x)){
                        good=false;
                        break;
                    }
                }
                if(good){
                    cnt++;
                }
                mp.clear();
            }
            else{
                StringTokenizer st=new StringTokenizer(s, " ");
                while(st.hasMoreTokens()){
                    String token=st.nextToken();
                    StringTokenizer wordTokenizer=new StringTokenizer(token, ":");
                    String word=wordTokenizer.nextToken();
                    boolean bad=false;
                    if(word.equals("byr")){
                        int year=Integer.parseInt(wordTokenizer.nextToken());
                        if(year<1920||year>2002){
                            bad=true;
                        }
                    }
                    else if(word.equals("iyr")){
                        int year=Integer.parseInt(wordTokenizer.nextToken());
                        if(year<2010||year>2020){
                            bad=true;
                        }
                    }
                    else if(word.equals("eyr")){
                        int year=Integer.parseInt(wordTokenizer.nextToken());
                        if(year<2020||year>2030){
                            bad=true;
                        }
                    }
                    else if(word.equals("hgt")){
                        String w=wordTokenizer.nextToken();
                        try{
                            int height=Integer.parseInt(w.substring(0, w.length()-2));
                            if(w.substring(w.length()-2, w.length()).equals("cm")){
                                if(height<150||height>193){
                                    bad=true;
                                }
                            }
                            else if(w.substring(w.length()-2, w.length()).equals("in")){
                                if(height<59||height>76){
                                    bad=true;
                                }
                            }
                            else{
                                bad=true;
                            }
                        }
                        catch (Exception e){
                            bad=true;
                        }


                    }
                    else if(word.equals("hcl")){
                        String w=wordTokenizer.nextToken();
                        if(w.length()==7){
                            char[] chars=w.toCharArray();
                            if(chars[0]!='#'){
                                bad=true;
                            }
                            for(int j=1; j<chars.length; ++j){
                                char c=chars[j];
                                if((c>='0' && c<='9') || (c>='a' && c<='f')){
                                    continue;
                                }
                                else{
                                    bad=true;
                                    break;
                                }
                            }
                        }
                        else{
                            System.out.println(token);
                            bad=true;
                        }
                    }
                    else if(word.equals("ecl")){
                        String w=wordTokenizer.nextToken();
                        String[] valid={"amb", "blu", "brn", "gry", "grn", "hzl","oth"};
                        boolean in=false;
                        for(String ss: valid){
                            if(w.equals(ss)){
                                in=true;
                                break;
                            }
                        }
                        if(!in) bad=true;
                    }
                    else if(word.equals("pid")){
                        String next=wordTokenizer.nextToken();
                        try{
                            int t=Integer.parseInt(next);
                            if(next.length()!=9){
                                bad=true;
                            }
                        }
                        catch (Exception e){
                            bad=true;
                        }
                    }
                    if(!bad)
                        mp.add(word);
                }
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

