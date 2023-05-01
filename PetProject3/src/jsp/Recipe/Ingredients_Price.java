package jsp.Recipe;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

import javax.imageio.ImageIO;

import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import java.lang.ClassNotFoundException;
/*
  자바 - 오라클데이터베이스 연동 프로그램
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
public class Ingredients_Price{

	public static void main(String[] args) throws ClassNotFoundException, SQLException, IOException {
		
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
//		sql = "select *from Ingredients_Price where i_name='식재료이름'";
////		  
//		Statement stmt = con.createStatement(); //web의 session같은 존재
//		
//		ResultSet result = stmt.executeQuery(sql);

//		5. update 명령문을 생성 및 실행
//		sql = "UPDATE Ingredients_Price SET i_name = ? WHERE i_price =?";
//		PreparedStatement stmt = con.prepareStatement(sql); 
//		stmt.setString(1,?);
//		stmt.setInt(2,?);
//		int result = stmt.executeUpdate();
//	    System.out.println("Update 결과 : " + result); 
		
//		if (result.next()) {
//			
//			String i_name = result.getString("i_name");			
//			Int i_price = result.getInt("i_price");
//			
//			
//
////		데이터 출력
//			System.out.println("i_name: " + i_name);
//			System.out.println("i_price: " + i_price);
//		}else {
//			System.out.println("레코드가 존재하지 않습니다.");
//			} 
//			
//		  
////		4-1. 4번 resultset close
//		result.close();  

//		6. insert 명령문을 생성 및 실행
		sql = "insert into Ingredients_Price(i_name, i_price)" +
			  "values(?,?)";
		PreparedStatement stmt = con.prepareStatement(sql); 
				
//		7 데이터 삽입(레코드세트)
		stmt.setString(1, "");
		stmt.setInt(2, 2000);
		
						
//		8. 4 or 5 close
		stmt.close();
		
//		9. 3번 close
		con.close();
		 
}}

	