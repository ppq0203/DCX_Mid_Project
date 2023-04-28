package jsp.Recipe;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

public class Recipe_Commend3 {

    public static void main(String[] args) {
        Connection conn = null;
        Statement stmt = null;
        ResultSet rs = null;

        try {
            // 1. JDBC 드라이버 로드 및 데이터베이스 연결 설정
            Class.forName("oracle.jdbc.driver.OracleDriver");
            String url = "jdbc:oracle:thin:@localhost:1521:XE";
            String user = "c##scott";
            String password = "tiger";
            conn = DriverManager.getConnection(url, user, password);

            // 2. 적절한 쿼리 작성 및 실행
            String query = "SELECT * FROM Ingredients_Img WHERE i_name='onion'";
            stmt = conn.createStatement();
            rs = stmt.executeQuery(query);

            // 3. 결과 파싱 및 필요한 정보 추출
            while (rs.next()) {
                String i_name = rs.getString("image_name");
                String image_url = rs.getString("image_path");
                String ingredientName = rs.getString("ingredient_name");
                
                // 4. 필요한 정보를 이용하여 원하는 작업 수행
                System.out.println("이미지 이름: " + i_name);
                System.out.println("이미지 경로: " + image_url);
                System.out.println("식재료 이름: " + ingredientName);
            }
        } catch (ClassNotFoundException e) {
            e.printStackTrace();
        } catch (SQLException e) {
            e.printStackTrace();
        } finally {
            // 5. 데이터베이스 연결 종료
            try {
                if (rs != null) rs.close();
                if (stmt != null) stmt.close();
                if (conn != null) conn.close();
            } catch (SQLException e) {
                e.printStackTrace();
            }
        }
    }
}

 
	

	