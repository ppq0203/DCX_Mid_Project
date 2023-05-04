package jsp.Recipe;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.io.IOException;
import java.lang.ClassNotFoundException;
/*
 * 자바 - 오라클데이터베이스 연동 프로그램
 * JDBC F/W사용
 * 1. driver 로딩
 * 2. 드라이버 관리자 등록
 * 3. 2번을 통해서 접속
 * 4. select 명령문을 생성 및 실행
 * 4-1. 4번 resultset close
 * 5. update 명령문을 생성 및 실행
 * 6. insert 명령문을 생성 및 실행
 * 7. 데이터 삽입(레코드세트)
 * 8. 4 or 5 close
 * 9. 3번 close
 * 
 */
public class Recipe_Content{

	public static void main(String[] args) throws SQLException, ClassNotFoundException, IOException {
		
//				
//		  자바 - 오라클데이터베이스 연동 프로그램
//		  JDBC F/W사용
//		  1. driver 로딩 --> CLASSPATH에서 찾는다.
//		ex)oracle DB 연결시
//		Class.forName("oracle.jdbc.driver.OracleDriver");
////		ex)mysql DB 연결실
////		Class.forName("com.mysql.jdbc.Driver");
////		  2. 드라이버 관리자 등록
////		  1번을 할 경우 자동 등록
////		  3. 2번을 통해서 접속
//		 String url = "";
//		 url = "jdbc:oracle:thin:@localhost:1521:XE";
//		  
////		  url = "jdbc:mysql://localhost:3306/DBNAME?characterEncoding=utf8&autoReconnect=true";
//		String user = "c##scott";
//		String password = "tiger";
//		Connection con = DriverManager.getConnection(url, user, password);
//		//sql문장
//		String sql = "";  
//		
////		4. select 명령문을 생성 및 실행
//		sql = "select *from Recipe_Content where r_num=";
////		  
//		Statement stmt = con.createStatement(); //web의 session같은 존재
//		ResultSet result = stmt.executeQuery(sql);
//		
////		5. update 명령문을 생성 및 실행
////		sql = "UPDATE Recipe_Content SET 컴럼 = ? WHERE 컬럼 =?";
////		PreparedStatement stmt = con.prepareStatement(sql); 
//		
////		stmt.setString(1,?);
////		stmt.setString(2,?);
////		int result = stmt.executeUpdate();
////		System.out.println("Update 결과 : " + result); 
////		ResultSet result = stmt.executeQuery(sql);
////				
//		if (result.next()) {
//			String r_num = result.getString("r_num");
//			String r_name = result.getString("r_name");
//
////		데이터 출력
//			System.out.println("r_num: " + r_num);
//			System.out.println("r_name: " + r_name);
//		}else {
//			System.out.println("레코드가 존재하지 않습니다.");
//		}  
//////		4-1. 4번을 close
////		result.close();  
//		
////		6. insert 명령문을 생성 및 실행
////		sql = "insert into Recipe_Content(r_num, r_name)" +
////			  "values(?,?)";
////		PreparedStatement stmt = con.prepareStatement(sql);
////		
//////		7. 데이터 삽입(레코드세트)
////		stmt.setString(1, "");
////		stmt.setString(2, "");
////		
		
////		8. 4 or 5 close
//		stmt.close();
////		9. 3번 close
//		con.close();
		
		//DAO에서 함수 호출하기 위한 준비
		IngredientDAO dao = new IngredientDAO();
		
		//csv 파일로 전체 입력하기
//		dao.CSV_Recipe_Content("C:\\Users\\anyware\\Desktop\\밥사조 프로젝트\\SNO_AND_ING.csv");
		dao.saveToCsv1("C:\\Users\\anyware\\Desktop\\밥사조 프로젝트\\test.csv");
		//1개 행 입력하기
//		dao.insertContent("","","");
		 
		 
		}}
	

	

	