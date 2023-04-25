package jsp.Recipe;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.lang.ClassNotFoundException;
/*
 * 자바 - 오라클데이터베이스 연동 프로그램
 * JDBC F/W사용
 * 1. driver 로딩
 * 2. 드라이버 관리자 등록
 * 3. 2번을 통해서 접속
 * 4. 명령문을 생성
 * 5. 명령문을 실행
 * 6. 결과테이블(레코드세트)
 * 7. 6번에서 데이터 get
 * 8. 6번을 close
 * 9. 4번 close
 * 10. 3번 close
 * 
 */
public class Ingredients_img{

	public static void main(String[] args) throws SQLException, ClassNotFoundException {
		
//		  자바 - 오라클데이터베이스 연동 프로그램
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
		sql = "select *from Ingredients_img where i_num=";
//		  
		Statement stmt = con.createStatement(); //web의 session같은 존재
		
		ResultSet result = stmt.executeQuery(sql);
//		 	
		if (result.next()) {
			long i_num = result.getLong("i_num");
			String im_name = result.getString("im_name");
			float color = result.getFloat("color");
			float length = result.getFloat("length");
			float weight = result.getFloat("weight");
			String image_url = result.getString("image_url");

//		데이터 출력
			System.out.println("i_num: " + i_num);
			System.out.println("im_name: " + im_name);
			System.out.println("color: " + color);
			System.out.println("length: " + length);
			System.out.println("weight: " + weight);
			System.out.println("image_url: " + image_url);
		}else {
			System.out.println("레코드가 존재하지 않습니다.");
		}  
//		4번을 close
		result.close();  
//		5. insert 명령문을 생성 및 실행
//		sql = "insert into Ingredients_img(i_num, im_name, color, length, weight,image_url )" +
//			  "values(?,?,?,?,?,?)";
//		PreparedStatement stmt = con.prepareStatement(sql); 
//		5-1 데이터 삽입(레코드세트)

//		stmt.setLong(1, L);
//		stmt.setString(2, "");
//		stmt.setFloat(3, "");
//		stmt.setFloat(4, "");
//		stmt.setFloat(5, "");
//		stmt.setString(6, "");
		
//		6. 4 or 5 close
		stmt.close();
//		7. 3번 close
		con.close();		 
	}}
	

 
	

	