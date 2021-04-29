package roaster.mapreduce;

import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;

public class Test {
    public static void main(String[] args) throws Exception {
        String value = "2015-01-01 16:00:00,246,246,249,370,363,344,548,546,536,363,349,356,282,286,277,194.7,8.030000000000001";
        String[] values = value.toString().split(",");
        String date=values[0];
        SimpleDateFormat newdate = new SimpleDateFormat("yyyy-MM-dd HH:mm");
        try {
            Date dates = newdate.parse(date);
            date=new SimpleDateFormat("yyyy-MM-dd HH:mm").format(dates);
        } catch (ParseException e) {
            e.printStackTrace();
        }

        if (values[17].split("\\.")[1].length()!=2){
            values[17] = String.format("%.2f",Double.parseDouble(values[17]));
        }

        if (values[16].split("\\.")[1].length()!=2) {
            values[16] = String.format("%.2f",Double.parseDouble(values[16]));
        }

        String result="";
        for (int i=0;i<values.length;i++){
            if (i==values.length-1){
                result=result+values[i];
            }else if (i==1) {
                result=date+"\t";
            }else {
                result=result+values[i]+"\t";
            }
        }
        System.out.println(result);

    }
}
