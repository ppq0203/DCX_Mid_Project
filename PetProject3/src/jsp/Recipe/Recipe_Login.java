package jsp.Recipe;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
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
 * 4. select 명령문을 생성 및 실행
 * 5. insert 명령문을 생성 및 실행
 * 5-1 데이터 삽입(레코드세트)
 * 6. 4 or 5 close
 * 7. 3번 close
 * 
 * 
 */
public class Recipe_Login{

	public static void main(String[] args) throws SQLException, ClassNotFoundException{
		
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
		sql = "select *from Recipe_Login where id='choi111'";
//		  
		Statement stmt = con.createStatement(); //web의 session같은 존재
		
		ResultSet result = stmt.executeQuery(sql);
//		 	
		if (result.next()) {
			String id = result.getString("id");
			String pw = result.getString("pw");
			long phone = result.getLong("phone");
			String address = result.getString("address");
			String email = result.getString("email");

//		데이터 출력
			System.out.println("id: " + id);
			System.out.println("pw: " + pw);
			System.out.println("phone: " + phone);
			System.out.println("address: " + address);
			System.out.println("email: " + email);
		}else {
			System.out.println("레코드가 존재하지 않습니다.");
		}  
//		4번을 close
		result.close();  
//		5. insert 명령문을 생성 및 실행
//		sql = "insert into Recipe_Login(id, pw, phone, address, email)" +
//				"values(?,?,?,?,?)";
//		PreparedStatement stmt = con.prepareStatement(sql); 
//		5-1 데이터 삽입(레코드세트)

//		stmt.setString(1, "");
//		stmt.setString(2, "");
//		stmt.setLong(3, );
//		stmt.setString(4, "");
//		stmt.setString(5, "");
		
//		6. 4 or 5 close
		stmt.close();
//		7. 3번 close
		con.close();
		 
}}
	

	

	