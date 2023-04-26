package jsp.Recipe;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

import javax.imageio.ImageIO;

import java.awt.image.BufferedImage;
import java.io.ByteArrayOutputStream;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStream;
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
 * 6-1 이미지 파일 저장하기 위한 준비
 * 7. 데이터 삽입(레코드세트)
 * 8. 4 or 5 close
 * 9. 3번 close
 */
public class Ingredients_Img{

	public static void main(String[] args) throws SQLException, ClassNotFoundException, IOException {
		
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
		sql = "select * from Ingredients_img";
//		sql = "select * from Ingredients_img where i_name=?"  
		Statement stmt = con.createStatement(); //web의 session같은 존재
		ResultSet result = stmt.executeQuery(sql);

//		5. update 명령문을 생성 및 실행
//		sql = "UPDATE Ingredients_img SET color = ? WHERE length =?";
//		PreparedStatement stmt = con.prepareStatement(sql);
//		
//		stmt.setString(1,"#74B230");
//		stmt.setFloat(2,400);
//		int result = stmt.executeUpdate();
//	    System.out.println("Update 결과 : " + result);
		
		while (result.next()) {
			String image_url = result.getString("image_url");
            File imageFile = new File(image_url);
			String i_name = result.getString("i_name");
			String color = result.getString("color");
			float length = result.getFloat("length");
			float weight = result.getFloat("weight");
			BufferedImage image = ImageIO.read(imageFile);
            ImageIO.write(image, "jpg", imageFile);
					  						
//		데이터 출력
			System.out.println("i_name: " + i_name);
			System.out.println("color: " + color);
			System.out.println("length: " + length+"cm");
			System.out.println("weight: " + weight+"g");
			System.out.println("image_url:" + image_url);
			} 
		 
//		4-1. 4번 resultset close
		result.close();  
		
//		6. insert 명령문을 생성 및 실행
//		sql = "insert into Ingredients_img(i_name, color, length, weight,image_url )" +
//			  "values(?,?,?,?,?)";
//		PreparedStatement stmt = con.prepareStatement(sql);
//		
////		6-1 이미지 파일 저장하기 위한 준비
//		String filename = "C://Users//anyware//Pictures//배추.jpg";

////		7 데이터 삽입(레코드세트)
//		stmt.setString(1, "배추");
//		stmt.setString(2, "#F76C35" );
//		stmt.setFloat(3, 400);
//		stmt.setFloat(4, 200);
//        stmt.setString(5, filename);
//		
//        stmt.executeUpdate();
//        System.out.println("이미지 경로를 저장하였습니다.");
//		8. 4 or 5 close
//		stmt.close();
//		9. 3번 close
//		con.close();	 
	}}

    

	

 
	

	