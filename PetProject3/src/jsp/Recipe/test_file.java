package jsp.Recipe;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class test_file {

    public static void main(String[] args) {
        String csvFilePath = "C:\\Users\\anyware\\Desktop\\밥사조 프로젝트\\table test\\test file.csv"; // CSV 파일 경로
        String newCsvFilePath = "C:\\Users\\anyware\\Desktop\\밥사조 프로젝트\\table test\\ingredient_classified.csv"; // 분류된 CSV 파일 경로
        Map<String, String[]> ingredientMap = new HashMap<String, String[]>(); // 식재료와 수량 정보를 담을 맵
        List<String> headerList = new ArrayList<String>(); // 새로운 CSV 파일의 헤더 정보를 담을 리스트
        headerList.addAll(Arrays.asList("재료", "수량")); // 헤더 정보 추가

        try {
            BufferedReader br = new BufferedReader(new FileReader(csvFilePath)); // CSV 파일 읽기
            String line;
            while ((line = br.readLine()) != null) {
                String[] ingredientInfo = line.split("\\|"); // '|' 기준으로 문자열 분리
                for (String info : ingredientInfo) {
                    String[] nameAndQuantity = info.trim().split(" "); // 공백을 기준으로 식재료와 수량 분리
                    String name = nameAndQuantity[0]; // 식재료 이름
                    String quantity = nameAndQuantity[1]; // 식재료 수량
                    int numIndex = quantity.indexOf("개");
                    int quantityNum = 0;
                                    
                    if (numIndex >= 0) {
                        quantityNum = Integer.parseInt(quantity.substring(0, numIndex));
                    }
                    if (!ingredientMap.containsKey(name)) {
                        ingredientMap.put(name, new String[] {name, quantity}); // 맵에 식재료와 수량 추가
                    } else {
                        String[] value = ingredientMap.get(name); // 맵에서 해당 식재료 정보 가져오기
                        String totalQuantity = calculateQuantity(value[1], quantity); // 기존 수량과 새로운 수량을 더한 값을 계산
                        ingredientMap.put(name, new String[] {name, totalQuantity}); // 맵에 식재료와 수량 추가
                    }
                }
            }
            br.close();

            FileWriter fw = new FileWriter(newCsvFilePath); // 분류된 CSV 파일 생성
            fw.append(String.join(",", headerList) + "\n"); // 헤더 정보 추가
            for (String[] value : ingredientMap.values()) {
                String lineStr = String.join(",", Arrays.asList(value));
                fw.append(lineStr + "\n"); // 식재료와 수량 정보 추가
            }
            fw.flush();
            fw.close();
            System.out.println("분류된 CSV 파일이 생성되었습니다.");

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
    private static int getGCD(int a, int b) {
        if (b == 0) {
            return a;
        }
        return getGCD(b, a % b);
    }
    private static String calculateQuantity(String originalQuantity, String newQuantity) {
        String[] originalQuantityArr = originalQuantity.split("/"); // 기존 수량을 분수 형태로 분리
        String[] newQuantityArr = newQuantity.split("/"); // 새로운 수량을 분수 형태로 분리
        int denominator = Integer.parseInt(originalQuantityArr[1]); // 분모
        int newDenominator = Integer.parseInt(newQuantityArr[1]); // 새로운 분모
        int numerator = Integer.parseInt(originalQuantityArr[0]) * (denominator / newDenominator); // 새로운 분모에 맞게 분자 계산

        // 기존 분모와 새로운 분모가 같을 경우 그대로 리턴
        if (denominator == newDenominator) {
            return originalQuantity;
        }

        // 새로운 분모가 기존 분모보다 작을 경우 분자만 계산하여 리턴
        if (newDenominator < denominator) {
            return numerator + "/" + newDenominator;
        }

        // 새로운 분모가 기존 분모보다 클 경우 새로운 분모에 맞게 분자 계산하여 리턴
        int remainder = denominator % newDenominator;
        if (remainder == 0) {
            return (numerator * (denominator / newDenominator)) + "/" + newDenominator;
        } else {
            int gcd = getGCD(newDenominator, remainder);
            int newNumerator = (numerator * (denominator / newDenominator)) + ((remainder / gcd) * Integer.parseInt(originalQuantityArr[0]));
            return newNumerator + "/" + (newDenominator / gcd);
        }
        
	
    }}
	