package jsp.Recipe;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class test_file2 {
    public static void main(String[] args) {
        String csvFile = "C:\\Users\\anyware\\Desktop\\밥사조 프로젝트\\table test\\test file.csv";
                        
                String line;
                String cvsSplitBy = "\\|";
                ArrayList<String[]> ingredients = new ArrayList<>();

                try (BufferedReader br = new BufferedReader(new FileReader(csvFile))) {
                    while ((line = br.readLine()) != null) {
                        String[] row = line.split(cvsSplitBy);
                        ingredients.add(row);
                    }
                } catch (IOException e) {
                    e.printStackTrace();
                }

                ArrayList<String[]> classifiedIngredients = new ArrayList<>();
                for (String[] ingredient : ingredients) {
                    for (int i = 0; i < ingredient.length; i += 2) {
                        String[] row = new String[2];
                        row[0] = ingredient[i].trim(); // 식재료
                        row[1] = ingredient[i+1].trim(); // 수량
                        classifiedIngredients.add(row);
                    }
                }
            
                try (FileWriter writer = new FileWriter("C:\\Users\\anyware\\Desktop\\밥사조 프로젝트\\table test\\output.csv")) {
                    for (String[] row : classifiedIngredients) {
                        writer.write(Arrays.toString(row) + "\n");
                    }
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        
    }

	