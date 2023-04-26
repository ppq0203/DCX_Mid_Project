package jsp.Recipe;
import java.sql.*;

public class Recipe_Commend2 {
    public static void main(String[] args) {
       
    	
        try {
            // 데이터베이스 연결
            Connection conn = DriverManager.getConnection("jdbc:oracle:thin:@localhost:1521:XE", "c##scott", "tiger");
            String sql= "";
            // 사용자가 등록한 식재료 조회
            sql = "SELECT i_name FROM Ingredients WHERE id = ?";
            PreparedStatement stmt = conn.prepareStatement(sql);
            stmt.setString(1, "choi123");
            ResultSet rs = stmt.executeQuery();
            
            // 추천 레시피 조회
            sql = "SELECT r_name FROM Recipe r " +
                                 "JOIN Recipe_Ingredients ri ON r.r_num = ri.r_num " +
                                 "WHERE ri.r_name IN (?) " +
                                 "GROUP BY r.r_num, r.r_name " +
                                 "HAVING COUNT(*) = (SELECT COUNT(*) FROM Ingredients WHERE id = ?)";
            PreparedStatement rstmt = conn.prepareStatement(sql);
            StringBuilder b = new StringBuilder();
            int count = 0;
            while (rs.next()) {
                if (count > 0) {
                    b.append(",");
                }
                b.append("?");
                rstmt.setString(++count, rs.getString(1));
            }
           
			rstmt.setString(1, b.toString());
            rstmt.setString(2, "choi123");
            ResultSet rrs = rstmt.executeQuery();

            // 추천 레시피 출력
            System.out.println("[" + "choi123" + "] 님께 추천하는 레시피 목록");
            while (rrs.next()) {
                System.out.println(rrs.getString(1));
            }

            // 연결 종료
            rrs.close();
            rstmt.close();
            rs.close();
            stmt.close();
            conn.close();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }
}
	

 
	

	