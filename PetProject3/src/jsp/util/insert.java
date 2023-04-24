package test.jdbc;

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
public class TestJDBC {

	public static void main(String[] args) throws ClassNotFoundException, SQLException {
		
//		  자바 - 오라클데이터베이스 연동 프로그램
//		  JDBC F/W사용
//		  1. driver 로딩 --> CLASSPATH에서 찾는다.
		Class.forName("oracle.jdbc.driver.OracleDriver");
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
//		  4. 명령문을 생성
		Statement Stmt = con.createStatement(); //web의 session같은 존재
		String sql = "";  //sql문장
//		  sql = "select table_name from tabs";	
//		  sql = "insert into Recipe_Login(id, pw, phone, address, email)" +
//				"values(), 0, 1,'0')";
		  sql = "select *from Recipe_Login";
//		  5. 명령문을 실행
//		  6. 결과테이블(레코드세트)
		ResultSet result = Stmt.executeQuery(sql);
//		  7. 6번에서 데이터 get
		String data = "";
		if (result.next()) {
		//ResultSet에서 getOoo()를 사용할 때 (int) or (Object) : int 인덱스(1번부터 시작), Object 컬럼명	
			data = result.getString(1); 	
//		}
		System.out.println("데이터 베이스 결과 :: " + data);
//		  8. 6번을 close
		result.close();
//		  9. 4번 close
		Stmt.close();
//		  10. 3번 close
		con.close();
		 
		 
		

	}}

	}