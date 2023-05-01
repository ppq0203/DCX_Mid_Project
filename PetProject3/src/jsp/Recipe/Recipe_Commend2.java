package jsp.Recipe;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class Recipe_Commend2 {

    public static void main(String[] args) {
    	// 파일에서 데이터를 읽어와서 List<String>에 저장
        List<String> lines = new ArrayList<>();
        try (BufferedReader br = new BufferedReader(new FileReader("C:\\Users\\anyware\\Desktop\\밥사조 프로젝트\\table test\\test2.csv"))) {
            String line;
            while ((line = br.readLine()) != null) {
                lines.add(line);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }

        // 각 재료를 |로 분리하여 CSV 파일로 저장
        try (BufferedWriter bw = new BufferedWriter(new FileWriter("C:\\Users\\anyware\\Desktop\\밥사조 프로젝트\\table test\\output2.txt"))) {
        	for (String line : lines) {
                String[] parts = line.split("\\d+", 2); // 숫자가 시작하는 지점부터 문자열을 분리
                if (parts.length == 2) { // 분리된 결과가 2개 이상인 경우에만 처리
                    String[] ingredients = parts[1].split("\\|"); // 재료를 |로 분리
                    for (String ingredient : ingredients) {
                        bw.write(ingredient.trim() + ","); // 재료를 CSV 파일로 저장
                    }
                    bw.newLine();
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
	

	