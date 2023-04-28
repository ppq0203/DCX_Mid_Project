package jsp.Recipe;
import java.sql.*;
import java.util.ArrayList;
import java.util.List;
public class Recipe_Commend {
    
	public static void main(String[] args) throws SQLException, ClassNotFoundException {
		// 데이터베이스 연결 정보
		// JDBC F/W사용
		// 1. driver 로딩 --> CLASSPATH에서 찾는다.
		// ex)oracle DB 연결시
		Class.forName("oracle.jdbc.driver.OracleDriver");
		// 2. 드라이버 관리자 등록
		// 1번을 할 경우 자동 등록
		// 3. 2번을 통해서 접속
		String url = "jdbc:oracle:thin:@localhost:1521:XE";
		String user = "c##scott";
		String password = "tiger";
		
		Connection con = DriverManager.getConnection(url, user, password);
		
		// id에 등록된 식재료를 가져오기 위한 쿼리문 생성
		String sql = "SELECT i_name FROM Ingredients WHERE id ='choi123'";
		 		
		Statement stmt = con.createStatement();
		ResultSet rs = stmt.executeQuery(sql);
		
		// id에 등록된 식재료를 저장하는 리스트 생성
		List<String> ingredientsList = new ArrayList<String>();
		while(rs.next()) {
			String i_name = rs.getString("i_name");
			ingredientsList.add(i_name);
		}		
		// 추천 레시피를 위한 쿼리문 생성
		String ingredientStr = String.join("', '", ingredientsList);
		
		sql = "SELECT r.r_name, r.r_category, r.r_time " +
		      "FROM Recipe r " +
		      "INNER JOIN Recipe_Ingredients ri ON r.r_num = ri.r_num " +
		      "INNER JOIN Ingredients i ON ri.r_name = i.i_name " +
		      "WHERE i.i_name IN ('" + ingredientStr + "') " +
		      "GROUP BY r.r_name, r.r_category, r.r_time " +
		      "HAVING COUNT(*) >= 3" +
		      "ORDER BY r.r_time ASC";
		stmt = con.createStatement();
		rs = stmt.executeQuery(sql);
		
		// 조건에 맞는 레시피의 이름, 종류, 조리시간을 담아서 출력
		while (rs.next()) {
			String r_name = rs.getString("r_name");
			String r_category = rs.getString("r_category");
			String r_time = rs.getString("r_time");
			System.out.println("레시피 이름: " + r_name);
			System.out.println("종류: " + r_category);
			System.out.println("조리시간: " + r_time);
		}

		rs.close();
		stmt.close();
		con.close();

	}
}

	

 
	

	