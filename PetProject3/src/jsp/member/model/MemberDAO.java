package jsp.member.model;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;
import java.sql.Date;

import javax.naming.NamingException;

import jsp.util.DBConnection;


/* Data Access Object
 * 테이블 당 한개의 DAO를 작성한다.
 * 
 * JSP_MEMBER 테이블과 연관된 DAO로
 * 회원 데이터를 처리하는 클래스이다.
 */
public class MemberDAO 
{
	private static MemberDAO instance;
	
	// 싱글톤 패턴
	public MemberDAO(){}
	public static MemberDAO getInstance(){
		if(instance==null)
			instance=new MemberDAO();
		return instance;
	}
	
	// String -> Date로 변경하는 메서드
	// 문자열로된 생년월일을 Date로 변경하기 위해 필요
	// java.util.Date클래스로는 오라클의 Date형식과 연동할 수 없다.
	// Oracle의 date형식과 연동되는 java의 Date는 java.sql.Date 클래스이다.
		
	// 회원정보를 JSP_MEMBER 테이블에 저장하는 메서드
	public void insertMember(MemberBean member) throws SQLException
	{	
		
		Connection conn = null;
		PreparedStatement pstmt = null;
		
		try {
			// 커넥션을 가져온다.
			System.out.println("pass");
			conn = DBConnection.getConnection();
			System.out.println("pass1");
			
			// 자동 커밋을 false로 한다.
			conn.setAutoCommit(false);
			System.out.println("pass2");
			
			// 쿼리 생성한다.
			// 가입일의 경우 자동으로 세팅되게 하기 위해 sysdate를 사용
			StringBuffer sql = new StringBuffer();
			System.out.println("pass3");
			sql.append("insert into Recipe_Login (id,pw,phone,address,email)values");
			sql.append("(?, ?, ?, ?, ?)");		
			
			/* 
			 * StringBuffer에 담긴 값을 얻으려면 toString()메서드를
			 * 이용해야 한다.
			 */
			pstmt = conn.prepareStatement(sql.toString());
			pstmt.setString(1, member.getId());
			pstmt.setString(2, member.getPw());		
			pstmt.setString(3, member.getMail1()+"@"+member.getMail2());
			pstmt.setString(4, member.getPhone());
			pstmt.setString(5, member.getAddress());
			
			// 쿼리 실행
			pstmt.executeUpdate();
			// 완료시 커밋
			conn.commit(); 
			
		} catch (ClassNotFoundException |  SQLException sqle) {
			// 오류시 롤백
			conn.rollback(); 
			
			throw new RuntimeException(sqle.getMessage());
		} finally {
			// Connection, PreparedStatement를 닫는다.
			try{
				if ( pstmt != null ){ pstmt.close(); pstmt=null; }
				if ( conn != null ){ conn.close(); conn=null;	}
			}catch(Exception e){
				throw new RuntimeException(e.getMessage());
			}
		} // end try~catch 
	} // end insertMember()
	
	
	// 로그인시 아이디, 비밀번호 체크 메서드
	// 아이디, 비밀번호를 인자로 받는다.
	public int loginCheck(String id, String password) 
	{
		Connection conn = null;
		PreparedStatement pstmt = null;
		ResultSet rs = null;

		String dbPW = ""; // db에서 꺼낸 비밀번호를 담을 변수
		int x = -1;

		try {
			// 쿼리 - 먼저 입력된 아이디로 DB에서 비밀번호를 조회한다.
			StringBuffer query = new StringBuffer();
			query.append("SELECT pw FROM Recipe_Login WHERE id=?");

			conn = DBConnection.getConnection();
			pstmt = conn.prepareStatement(query.toString());
			pstmt.setString(1, id);
			rs = pstmt.executeQuery();

			if (rs.next()) // 입려된 아이디에 해당하는 비번 있을경우
			{
				dbPW = rs.getString("pw"); // 비번을 변수에 넣는다.

				if (dbPW.equals(password)) 
					x = 1; // 넘겨받은 비번과 꺼내온 배번 비교. 같으면 인증성공
				else 				 
					x = 0; // DB의 비밀번호와 입력받은 비밀번호 다름, 인증실패
				
			} else {
				x = -1; // 해당 아이디가 없을 경우
			}

			return x;

		} catch (Exception sqle) {
			throw new RuntimeException(sqle.getMessage());
		} finally {
			try{
				if ( pstmt != null ){ pstmt.close(); pstmt=null; }
				if ( conn != null ){ conn.close(); conn=null;	}
			}catch(Exception e){
				throw new RuntimeException(e.getMessage());
			}
		}
	} // end loginCheck()
	 
    
	public ArrayList<MemberBean> memberList() throws ClassNotFoundException, NamingException{
    	
		// 회원정보 저장 배열 (가변길이)
		ArrayList<MemberBean> mList = new ArrayList<MemberBean>();
		Connection conn = null;
		PreparedStatement pstmt = null;
		
		String sql = "";
        
		try {
			ResultSet rs = null;
			conn = DBConnection.getConnection();
			// 3. sql 작성 (select) & pstmt 객체
			sql = "select * from Recipe_Login where id != ?";
			pstmt = conn.prepareStatement(sql);
			pstmt.setString(1, "id");
					// 4. sql 실행
			rs = pstmt.executeQuery();
			
					// 5. 데이터 처리
			 // 이메일을 @ 기준으로 자른다.
            
			
            while(rs.next()) {
            	String mail = rs.getString("mail");
                int idx = mail.indexOf("@"); 
                String mail1 = mail.substring(0, idx);
                String mail2 = mail.substring(idx+1);
				//데이터 있을 때 마다!!!!!!!!!!
				//디비(테이블 정보) -> MemberBean -> ArrayList에 넣기 
				MemberBean mb = new MemberBean();
				mb.setId(rs.getString("id"));
				mb.setPw(rs.getString("pw"));
				mb.setMail1(mail1);
				mb.setMail2(mail2);
				
				
					//MemberBean -> ArrayList 
				mList.add(mb);
				
			} //if 끝나고 나면 메시지 하나 찎어보기
			
		} catch (Exception e) {
			e.printStackTrace();
		}finally {
			try {
				conn.close();
				pstmt.close();
			} catch (SQLException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
			
			
		}
		
		return mList;	
		}
	
	
	//회원정보 조회(all) - memberList();
 //class

 
    public MemberBean getUserInfo(String id) 
    {
        Connection conn = null;
        PreparedStatement pstmt = null;
        ResultSet rs = null;
        MemberBean member = null;
 
        try {
            // 쿼리
            StringBuffer query = new StringBuffer();
            query.append("SELECT * FROM Recipe_Login WHERE id=?");
 
            conn = DBConnection.getConnection();
            pstmt = conn.prepareStatement(query.toString());
            pstmt.setString(1, id);
            rs = pstmt.executeQuery();
 
            if (rs.next()) // 회원정보를 DTO에 담는다.
            {
                
                // 이메일을 @ 기준으로 자른다.
                String mail = rs.getString("mail");
                int idx = mail.indexOf("@"); 
                String mail1 = mail.substring(0, idx);
                String mail2 = mail.substring(idx+1);
                
                // 자바빈에 정보를 담는다.
                member = new MemberBean();
                member.setId(rs.getString("id"));
                member.setPw(rs.getString("pw"));                
                member.setMail1(mail1);
                member.setMail2(mail2);
                member.setPhone(rs.getString("phone"));
                member.setAddress(rs.getString("address"));
                
           
            }
 
            return member;
 
        } catch (Exception sqle) {
            throw new RuntimeException(sqle.getMessage());
        } finally {
            // Connection, PreparedStatement를 닫는다.
            try{
                if ( pstmt != null ){ pstmt.close(); pstmt=null; }
                if ( conn != null ){ conn.close(); conn=null;    }
            }catch(Exception e){
                throw new RuntimeException(e.getMessage());
            }
        }
    }    // end getUserInfo
    
    
public void updateMember(MemberBean member) throws SQLException{
        
        Connection conn = null;
        PreparedStatement pstmt = null;
 
        try {
 
            StringBuffer query = new StringBuffer();
            query.append("UPDATE Recipe_Login SET");
            query.append("  PW=?, PHONE=?, ADDRESS=?");
            query.append(" WHERE ID=?");
          
            
            conn = DBConnection.getConnection();
            pstmt = conn.prepareStatement(query.toString());
            
            // 자동 커밋을 false로 한다.
            conn.setAutoCommit(false);
           
            
            pstmt.setString(1, member.getPw());  
            pstmt.setString(2, member.getMail1()+"@"+member.getMail2());
            pstmt.setString(3, member.getPhone());
            pstmt.setString(4, member.getAddress());
            pstmt.setString(5, member.getId());
 
            pstmt.executeUpdate();
            // 완료시 커밋
            conn.commit(); 
                        
        } catch (Exception sqle) {
            conn.rollback(); // 오류시 롤백
            throw new RuntimeException(sqle.getMessage());
        } finally {
            try{
                if ( pstmt != null ){ pstmt.close(); pstmt=null; }
                if ( conn != null ){ conn.close(); conn=null;    }
            }catch(Exception e){
                throw new RuntimeException(e.getMessage());
            }
        }
    } // end updateMember
    
    @SuppressWarnings("resource")
    public int deleteMember(String id, String pw) 
    {
        Connection conn = null;
        PreparedStatement pstmt = null;
        ResultSet rs = null;
 
        String dbpw = ""; // DB상의 비밀번호를 담아둘 변수
        int x = -1;
 
        try {
            // 비밀번호 조회
            StringBuffer query1 = new StringBuffer();
            query1.append("SELECT PW FROM Recipe_Login WHERE ID=?");
 
            // 회원 삭제
            StringBuffer query2 = new StringBuffer();
            query2.append("DELETE FROM Recipe_Login WHERE ID=?");
 
            conn = DBConnection.getConnection();
 
            // 자동 커밋을 false로 한다.
            conn.setAutoCommit(false);
            
            // 1. 아이디에 해당하는 비밀번호를 조회한다.
            pstmt = conn.prepareStatement(query1.toString());
            pstmt.setString(1, "id");
            rs = pstmt.executeQuery();
 
            if (rs.next()) 
            {
                dbpw = rs.getString("pw");
                if (dbpw.equals(pw)) // 입력된 비밀번호와 DB비번 비교
                {
                    // 같을경우 회원삭제 진행
                    pstmt = conn.prepareStatement(query2.toString());
                    pstmt.setString(1, id);
                    pstmt.executeUpdate();
                    conn.commit(); 
                    x = 1; // 삭제 성공
                } else {
                    x = 0; // 비밀번호 비교결과 - 다름
                }
            }
 
            return x;
 
        } catch (Exception sqle) {
            try {
                conn.rollback(); // 오류시 롤백
            } catch (SQLException e) {
                e.printStackTrace();
            }
            throw new RuntimeException(sqle.getMessage());
        } finally {
            try{
                if ( pstmt != null ){ pstmt.close(); pstmt=null; }
                if ( conn != null ){ conn.close(); conn=null;    }
            }catch(Exception e){
                throw new RuntimeException(e.getMessage());
            }
        }
    } // end deleteMember
}

	


