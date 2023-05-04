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

import jsp.Recipe.IngredientDAO;
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
 * 8. delete 명령문을 생성 및 실행
 * 8-1. 데이터 삽입
 * 9. 4 or 5 close
 * 10. 3번 close
 */
public class Ingredients{

	public static void main(String[] args) throws ClassNotFoundException, SQLException, IOException {
		
//		  자바 - 오라클데이터베이스 연동 프로그램
//		  JDBC F/W사용
//		  1. driver 로딩 --> CLASSPATH에서 찾는다.
//		ex)oracle DB 연결시
//		Class.forName("oracle.jdbc.driver.OracleDriver");
//////		ex)mysql DB 연결실
////		Class.forName("com.mysql.jdbc.Driver");
//////		  2. 드라이버 관리자 등록
//////		  1번을 할 경우 자동 등록
//////		  3. 2번을 통해서 접속
//		 String url = "";
//		 url = "jdbc:oracle:thin:@localhost:1521:XE";
////		  
////		  url = "jdbc:mysql://localhost:3306/DBNAME?characterEncoding=utf8&autoReconnect=true";
//		String user = "c##scott";
//		String password = "tiger";
//		Connection con = DriverManager.getConnection(url, user, password);
////		//sql문장
//		String sql = "";  
////		4 select 명령문을 생성 및 실행
//		sql = "select *from Ingredients where id='choi123'";
//		  
//		Statement stmt = con.createStatement(); //web의 session같은 존재
//		
//		ResultSet result = stmt.executeQuery(sql);
////
//////		5. update 명령문을 생성 및 실행
//		sql = "UPDATE Ingredients SET i_name = ? WHERE id =?";
//		PreparedStatement stmt = con.prepareStatement(sql); 
//		stmt.setString(1,"오이");
//		stmt.setString(2,"choi123");
//		int result = stmt.executeUpdate();
//	    System.out.println("Update 결과 : " + result); 
////		
//		if (result.next()) {
//			
//			String id = result.getString("id");			
//			String i_name = result.getString("i_name");
//			long i_quantity = result.getLong("i_quantity");
//			
//
////		데이터 출력
//			System.out.println("id: " + id);
//			System.out.println("i_name: " + i_name);
//			System.out.println("i_quantity: " + i_quantity);
//		}else {
//			System.out.println("레코드가 존재하지 않습니다.");
//			} 
////			
////		  
//////		4-1. 4번 resultset close
////		result.close();  
//
////		6. insert 명령문을 생성 및 실행
////		sql = "insert into Ingredients(id, i_name, i_quantity)" +
////			  "values(?,?,?)";
////		PreparedStatement stmt = con.prepareStatement(sql); 
////				
//////		7 데이터 삽입(레코드세트)
////		stmt.setString(1, "choi111");
////		stmt.setString(2, "배추");
////		stmt.setLong(3, 1L);
////		
////		8. delete 명령문을 생성 및 실행
////		String i_name = "";
////		sql = "delete from Ingredients where id = ? and i_name=?";
////		PreparedStatement stmt = con.prepareStatement(sql);	
////		
//////		8-1. 데이터 삽입
////		stmt.setString(1, "");
////		stmt.setString(2, "");
////		
////		int rows = stmt.executeUpdate();
////		//결과 출력
////		if (rows == 1) {
////            System.out.println(i_name + " 재료가 삭제되었습니다.");
////        } else {
////            System.out.println(i_name + " 재료가 존재하지 않습니다.");
////        }
////		9. 4 or 5 close
//		stmt.close();
//		
////		10. 3번 close
//		con.close();
		
		//DAO에서 함수 호출하기 위한 준비
		IngredientDAO i_dao = new IngredientDAO();
		
		//새로운 데이타 1행 입력
		i_dao.insertIngredient("asdfasf", "대파", 1f, "ea");
				
		//ID에 입력된 재료와 수량 조회
//		RecipeDTO result = i_dao.selectIngredient("id");
//		if (result != null) {
//			System.out.println("아이디: " + result.getId());
//			System.out.println("재료명: " + result.getING_NAME());
//			System.out.println("보유량: " + result.getING_AMOUNT() + result.getING_UNIT());
//		}		
		//ID와 재료명으로 데이터 수정 및 삭제
//		i_dao.updateIngredient("dkqydhd", "양파");
//		i_dao.deleteIngredient("asdfasf", "대파");
		
	}}

	