package jsp.Recipe;

import java.io.BufferedReader;
import java.io.FileOutputStream;
import java.io.FileReader;
import java.io.IOException;
import java.io.OutputStreamWriter;
import java.io.UnsupportedEncodingException;
import java.io.Writer;
import java.nio.charset.StandardCharsets;
import java.util.ArrayList;
import java.util.List;

public class test_file3 {

    public static void main(String[] args) throws UnsupportedEncodingException {
        String csvFilePath = "C:\\Users\\anyware\\Desktop\\밥사조 프로젝트\\table test\\ingredient_quantities.csv";
        csvFilePath = new String(csvFilePath.getBytes("UTF-8"), "UTF-8");
        String line = "";
        String cvsSplitBy = ",";
        
        System.out.println(line);
        List<String> ingredients = new ArrayList<>();
       
        
        try (BufferedReader br = new BufferedReader(new FileReader(csvFilePath))) {
            while ((line = br.readLine()) != null) {
                String[] recipe = line.split(cvsSplitBy);
                
               
                if (recipe.length >= 10) {  // CSV 파일의 각 줄이 적어도 두 개의 요소를 가져야 함
                    ingredients.add(recipe[0]);
                    
                }
            }
            FileOutputStream fos = new FileOutputStream("C:\\Users\\anyware\\Desktop\\밥사조 프로젝트\\table test\\ingredient1.txt");
            Writer writer = new OutputStreamWriter(fos, StandardCharsets.UTF_8);
            for (int i = 0; i < ingredients.size(); i++) {
                writer.write(ingredients.get(i)+ "\n");
            }
            writer.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}







	