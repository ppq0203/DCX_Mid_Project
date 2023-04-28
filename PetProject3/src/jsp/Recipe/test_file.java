package jsp.Recipe;

import java.io.BufferedReader;
import java.io.FileOutputStream;
import java.io.FileReader;
import java.io.IOException;
import java.io.OutputStreamWriter;
import java.io.Writer;
import java.nio.charset.StandardCharsets;
import java.util.ArrayList;
import java.util.List;

public class test_file {
    public static void main(String[] args) {
        String csvFilePath = "C:\\Users\\anyware\\Desktop\\밥사조 프로젝트\\table test\\test.csv";
        String line = "";
        String cvsSplitBy = "\\|";
        List<String> ingredients = new ArrayList<>();
        
        try (BufferedReader br = new BufferedReader(new FileReader(csvFilePath))) {
            while ((line = br.readLine()) != null) {
                String[] recipe = line.split(cvsSplitBy);
                String name = recipe[0];    
                String number = recipe[1];
                ingredients.add(name);
            }System.out.println(ingredients);
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






	