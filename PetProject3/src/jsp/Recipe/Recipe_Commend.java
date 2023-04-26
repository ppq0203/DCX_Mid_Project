package jsp.Recipe;
import java.sql.*;

public class Recipe_Commend {
    
	public static void main(String[] args) throws SQLException, ClassNotFoundException {
        // 데이터베이스 연결 정보
//    	  자바 - 오라클데이터베이스 연동 프로그램
//		  JDBC F/W사용
//		  1. driver 로딩 --> CLASSPATH에서 찾는다.
//		ex)oracle DB 연결시
		Class.forName("oracle.jdbc.driver.OracleDriver");
//		ex)mysql DB 연결실
//		Class.forName("com.mysql.jdbc.Driver");
//		  2. 드라이버 관리자 등록
//		  1번을 할 경우 자동 등록
//		  3. 2번을 통해서 접속
		 String url = "";
		 url = "jdbc:oracle:thin:@localhost:1521:XE";
		  
//		  url = "jdbc:mysql://localhost:3306/DBNAME?characterEncoding=utf8&autoReconnect=true";
		String user = "c##scott";
		String password = "tiger";
		Connection con = DriverManager.getConnection(url, user, password);
		//sql문장
		String sql = "";  
    
   //		4 select 명령문을 생성 및 실행
//		sql = "select *from Recipe_Login where id='choi111'";
//			        
	    Statement stmt = null;
	    ResultSet rs = null;
	    
	          	           
	       stmt = con.createStatement();
	        sql = "SELECT r.r_name, r.r_category, r.r_time " +
	                      "FROM Recipe r " +
	                      "INNER JOIN Recipe_Ingredients ri ON r.r_num = ri.r_num " +
	                      "INNER JOIN Ingredients i ON ri.r_name = i.i_name " +
	                      "WHERE i.i_name IN ('ingredient1', 'ingredient2', 'ingredient3') " +
	                      "GROUP BY r.r_name, r.r_category, r.r_time " +
	                      "HAVING COUNT(*) = 1 " +
	                      "ORDER BY r.r_time ASC";
	         rs = stmt.executeQuery(sql);

	            // Process the result set
	         while (rs.next()) {
	             String r_name = rs.getString("r_name");
	             String r_category = rs.getString("r_category");
	             long r_time = rs.getLong("r_time");
	             System.out.println("레시피 이름: " + r_name);
	             System.out.println("종류: " + r_category);
	             System.out.println("조리시간: " + r_time);
	             				}
	     
          
              rs.close();
	          stmt.close();
	          con.close();
	          
	     }
	    }
	

	

 
	

	