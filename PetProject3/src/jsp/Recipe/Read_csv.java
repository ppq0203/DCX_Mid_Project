package jsp.Recipe;


import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;

public class Read_csv {
    public static void main(String[] args) throws SQLException, IOException {
        String jdbcUrl = "jdbc:oracle:thin:@localhost:1521:xe";
        String username = "c##scott";
        String password = "tiger";
        String csvFilePath = "C:\\Users\\anyware\\Desktop\\밥사조 프로젝트\\table test\\RecipeAll.csv";
        
        Connection connection = DriverManager.getConnection(jdbcUrl, username, password);
            BufferedReader br = new BufferedReader(new FileReader(csvFilePath)); 
            
            String line;
            String tableName = "Recipe";
            String insertSql = "INSERT INTO " + tableName + " (r_num, r_name, servings, r_level, r_time,r_recommend, r_category) VALUES (?, ?, ?, ?, ?, ?, ?)";
            PreparedStatement pstmt = connection.prepareStatement(insertSql);
            
            // CSV 파일의 첫 번째 줄은 열 이름으로 제외시킴
            br.readLine();
            
            
            while ((line = br.readLine()) != null) {
                String[] values = line.split(",");
                pstmt.setInt(1, Integer.parseInt(values[0]));
                pstmt.setString(2, values[1]);
                pstmt.setString(3, values[2]);
                pstmt.setString(4, values[3]);
                pstmt.setString(5, values[4]);
                pstmt.setInt(6, Integer.parseInt(values[5]));
                pstmt.setString(7, values[6]);
                
                
                pstmt.executeUpdate();
            }
            
            System.out.println("CSV file has been imported into the database.");
            
       
    }
}
	

 
	

	