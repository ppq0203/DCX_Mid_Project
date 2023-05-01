<%@page import="java.lang.reflect.Member"%>
<%@page import="javax.management.MBeanAttributeInfo"%>
<%@ page language="java" contentType="text/html; charset=EUC-KR"
    pageEncoding="EUC-KR"%>
<%@ page import="jsp.member.model.MemberDAO" %>    
<%@ page import="jsp.member.model.MemberBean" %>
<%@ page import="java.util.ArrayList" %>
<html>
<head>
    <title>현재 유저정보 출력화면</title>
    <link href='../../css/join_style.css' rel='stylesheet' style='text/css'/>
  
    <%
    request.setCharacterEncoding("euc-kr");
	String id = request.getParameter("id");
	
	
	//DB에 저장된 회원정보를 모두 가져오기
	
	MemberDAO dao = new MemberDAO();    
        // 세션에 저장된 아이디를 가져와서
        // 그 아이디 해당하는 회원정보를 가져온다.
      MemberBean mb = dao.getUserInfo(id); 
    // memberBean = dao.getUserInfo(id);
    %>
    <script type="text/javascript">
    
        function changeForm(val){
            if(val == "-1"){
                history.back();
            }else if(val == "0"){
            	location.href="ModifyForm.jsp?id=<%=mb.getId()%>";
            
            }else if(val == "1"){
                location.href="DeleteForm.jsp?id=<%=mb.getId()%>";
                
            }
        }
        
    </script>
    
</head>
<body>
	
	
    
 <div id="wrap"> 
       
        <b><font size="6" color="gray">회원 정보</font></b>
      
                        <!-- 가져온 회원정보를 출력한다. -->
            <form method="post" action="../view/ModifyForm.jsp" name="Info">       
        <table>
            <tr>
                <td id="title">아이디</td>
                <td><%=mb.getId()%></td>
            </tr>
                      
            <tr>
                <td id="title">이메일</td>
                <td>
                    <%=mb.getMail1() %>@
                    <%=mb.getMail2() %>
                </td>
            </tr>
                    
            <tr>
                <td id="title">휴대전화</td>
                <td><%=mb.getPhone() %></td>
            </tr>
            <tr>
                <td id="title">주소</td>
                <td><%=mb.getAddress()%></td>
            </tr>
            </table>
            <br>
             <input type="button" value="뒤로" onclick="changeForm(-1)">
             <input type="button" value="회원정보수정" onclick="changeForm(0)">
       
             <input type="button" value="회원탈퇴" onclick="changeForm(1)">
         
        
        </form>
         </div> 
        <br>
        
</body>
</html>
